from typing import List

import aiohttp

from db.farm_repo import delete_farm, insert_farm, insert_wallet
from infrastructure.farm.prepare_farm_data import prepare_farm_data


async def add_wallet_to_farm(
    user_id: int, new_wallets: List[str], session: aiohttp.ClientSession, chain: str
):
    await delete_farm(user_id)
    request, wallets, total = await prepare_farm_data(
        user_id, new_wallets, session, chain
    )
    farm_id = await insert_farm(user_id, chain, total)
    for wallet in wallets:
        await insert_wallet(farm_id, chain, wallet)
    request = "Поздравляем, новая ферма успешно создана!\n\n" + request
    return request
