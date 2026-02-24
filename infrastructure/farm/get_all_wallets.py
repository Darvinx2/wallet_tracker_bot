from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from db.farm_repo import FarmRepository


async def get_requests(user_id: int, wallets: List[str], db_session: AsyncSession) -> List[str]:
    db = FarmRepository(db_session)

    wallets_db = await db.get_farm_wallet(user_id)

    if wallets_db:
        wallets.extend(wallets_db)

    return wallets
