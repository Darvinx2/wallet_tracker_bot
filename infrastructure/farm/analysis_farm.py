import aiohttp

from db.farm_repo import get_farm_wallet, get_last_date, get_total
from infrastructure.farm.update_farm import update_farm


async def total_wallets(user_id: int) -> int:
    bd_wallets = await get_farm_wallet(user_id)
    wallets = bd_wallets["array_agg"] or []
    count_wallets = len(wallets)
    return count_wallets


async def get_answer(user_id: int, session: aiohttp.ClientSession):
    old_total = round(await get_total(user_id), 2)
    request = await update_farm(user_id, [], session, "solana")
    new_total = await get_total(user_id)
    last_date = await get_last_date(user_id)
    old_balance = f"Баланс последней проверки {last_date}: {old_total}$\n"
    pnl = round(old_total - new_total, 2)
    ans_pnl = f"PNL фермы с последней проверки {last_date}: {pnl}$\n\n"
    count_wallet = await total_wallets(user_id)
    ans_count_wallet = f"Всего кошельков: {count_wallet}\n\n"
    answer = old_balance + ans_pnl + ans_count_wallet + request
    return answer
