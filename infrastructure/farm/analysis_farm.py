import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from db.farm_repo import FarmRepository
from infrastructure.farm.update_farm import update_farm


async def total_wallets(user_id: int, db_session: AsyncSession) -> int:
    db = FarmRepository(db_session)
    wallets = await db.get_farm_wallet(user_id)
    count_wallets = len(wallets)
    return count_wallets


async def get_answer(user_id: int, session: aiohttp.ClientSession, db_session: AsyncSession):
    db = FarmRepository(db_session)
    old_total = round(await db.get_total(user_id), 2)
    request = await update_farm(user_id, [], session, "solana", db_session)
    new_total = await db.get_total(user_id)
    last_date = await db.get_last_date(user_id)
    old_balance = f"Баланс последней проверки {last_date}: {old_total}$\n"
    pnl = round(old_total - new_total, 2)
    ans_pnl = f"PNL фермы с последней проверки {last_date}: {pnl}$\n\n"
    count_wallet = await total_wallets(user_id, db_session)
    ans_count_wallet = f"Всего кошельков: {count_wallet}\n\n"
    answer = old_balance + ans_pnl + ans_count_wallet + request
    return answer
