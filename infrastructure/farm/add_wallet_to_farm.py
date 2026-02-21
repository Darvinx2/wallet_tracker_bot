from typing import List

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from db.farm_repo import delete_farm, FarmAccsessor
from infrastructure.farm.prepare_farm_data import prepare_farm_data


async def add_wallet_to_farm(
        user_id: int,
        new_wallets: List[str],
        session: aiohttp.ClientSession,
        chain: str,
        db_session: AsyncSession
) -> object:
    db = FarmAccsessor(db_session)
    await delete_farm(user_id)
    request, wallets, total = await prepare_farm_data(
        user_id, new_wallets, session, chain
    )
    farm_id = await db.insert_farm(user_id, chain, total)
    for wallet in wallets:
        await db.insert_wallet(farm_id, chain, wallet)
    request = "Поздравляем, новая ферма успешно создана!\n\n" + request
    return request
