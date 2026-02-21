import logging

import aiohttp
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from data.text import CHOSE_CHAIN_TEXT, EDIT_FARM_TEXT
from decorator.log_handlers import log_callback
from handlers.farm.farm_state import FarmState
from infrastructure.farm.update_farm import update_farm
from keyboards.kb_chose_chain import chose_keyboard_kb
from keyboards.kb_edit_farm import edit_farm_kb
from keyboards.kb_exit_to_chose_chain import exit_to_chose_chain_kb

router = Router()

logger = logging.getLogger("farm_edit")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == "edit_farm")
@log_callback(logger)
async def edit_farm(callback: types.CallbackQuery):
    await callback.message.edit_text(text=EDIT_FARM_TEXT, reply_markup=edit_farm_kb())


@router.callback_query(F.data == "recreate_farm")
@log_callback(logger)
async def recreate_farm(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(FarmState.waiting_farm)
    await callback.message.edit_text(
        text=CHOSE_CHAIN_TEXT, reply_markup=chose_keyboard_kb()
    )


@router.callback_query(F.data == "expand_farm")
@log_callback(logger)
async def expand_farm(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(FarmState.waiting_update_wallets)
    await callback.message.edit_text(
        text=CHOSE_CHAIN_TEXT, reply_markup=chose_keyboard_kb()
    )


@router.message(FarmState.waiting_update_wallets)
@log_callback(logger)
async def update_wallets(
    message: types.Message, state: FSMContext, session: aiohttp.ClientSession, db_session: AsyncSession,
):
    user_id = message.from_user.id
    data = await state.get_data()
    chain = data["chain"]
    new_wallets = message.text.splitlines()
    request = await update_farm(user_id, new_wallets, session, chain, db_session)
    request = "Ферму успешно расширена!\n\n" + request
    await state.clear()
    await message.answer(text=request, reply_markup=exit_to_chose_chain_kb())
