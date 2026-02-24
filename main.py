import asyncio
import logging

from aiogram import Bot, Dispatcher

from data.config import BOT_TOKEN
from db.database import session
from handlers import (balance_abstract, balance_evm, balance_menu, drop_menu,
                      error, fallback, main_menu)
from handlers.farm import farm_analysis, farm_edit, farm_start_menu
from handlers.solana import balance_solana
from middleware.session_middleware import AiohttpMiddleware

file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
file_handler.setFormatter(formatter)

for name in [
    "base_api",
    "moralis_api",
    "jupiter_api",
    "formatting",
    "main_menu",
    "balance_menu",
    "balance_evm",
    "balance_abstract",
    "balance_solana",
    "fallback",
    "error",
    "drop_menu",
    "farm_start_menu",
    "farm_edit",
    "farm_analysis",
]:
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    middleware = AiohttpMiddleware(session_maker=session)
    dp.update.middleware(middleware=middleware)

    dp.include_router(main_menu.router)
    dp.include_router(balance_menu.router)
    dp.include_router(balance_evm.router)
    dp.include_router(balance_abstract.router)
    dp.include_router(balance_solana.router)
    dp.include_router(drop_menu.router)
    dp.include_router(farm_start_menu.router)
    dp.include_router(farm_edit.router)
    dp.include_router(farm_analysis.router)
    dp.include_router(error.router)
    dp.include_router(fallback.router)

    await middleware.start()
    try:
        await dp.start_polling(bot)
    finally:
        await middleware.stop()


if __name__ == "__main__":
    asyncio.run(main())
