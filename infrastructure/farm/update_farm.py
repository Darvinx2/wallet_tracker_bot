from typing import List

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from db.farm_repo import (
    get_farm_wallet,
    update_total,
    FarmAccsessor,
)
from infrastructure.farm.prepare_farm_data import prepare_farm_data


async def update_farm(
    user_id: int, new_wallets: List[str], session: aiohttp.ClientSession, chain: str, db_session: AsyncSession
):
    db = FarmAccsessor(db_session)
    db_row = await get_farm_wallet(user_id)
    wallets_db = db_row["array_agg"]
    request_wallet = []
    if new_wallets:
        request_wallet.extend(new_wallets)
    if wallets_db:
        request_wallet.extend(wallets_db)
    request, wallets, total = await prepare_farm_data(
        user_id, request_wallet, session, chain
    )
    await update_total(total, user_id)

    farm_id = await db.get_farm_id(user_id)
    for wallet in new_wallets:
        await db.insert_wallet(farm_id, chain, wallet)

    return request
