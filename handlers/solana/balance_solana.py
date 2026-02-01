import logging

import aiohttp
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from data.text import BAlANCE_SOLANA_TEXT
from decorator.log_handlers import log_callback
from handlers.solana.solana_state import SolanaState
from infrastructure.solana_api.api_request import api_request
from keyboards.kb_balance_solana import balance_solana_kb

router = Router()

logger = logging.getLogger("balance_solana")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == "balance_solana")
@log_callback(logger)
async def balance_solana(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(SolanaState.waiting_wallet)
    logger.info("Update state waiting_wallet")
    await callback.message.edit_text(
        text=BAlANCE_SOLANA_TEXT, reply_markup=balance_solana_kb()
    )


@router.message(SolanaState.waiting_wallet)
async def show_solana_balance(
    message: types.Message, state: FSMContext, session: aiohttp.ClientSession
) -> None:
    wallets = message.text.splitlines()
    request = await api_request(wallets, session)
    await message.answer(text=request, reply_markup=balance_solana_kb())
    await state.clear()
