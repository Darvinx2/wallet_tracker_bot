from typing import List

from db.farm_repo import get_farm_wallet


async def get_requests(user_id: int, wallets: List[str]) -> List[str]:
    db_row = await get_farm_wallet(user_id)

    wallets_db = db_row["array_agg"]

    if wallets_db:
        wallets.extend(wallets_db)

    return wallets
