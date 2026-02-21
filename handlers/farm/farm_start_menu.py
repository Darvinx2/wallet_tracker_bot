import logging

import aiohttp
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from data.text import CHOSE_CHAIN_TEXT, CREATE_FARM_TEXT, FARM_MENU_TEXT, SOON
from db.farm_repo import FarmAccsessor
from decorator.log_handlers import log_callback
from handlers.farm.farm_state import FarmState
from infrastructure.farm.add_wallet_to_farm import add_wallet_to_farm
from keyboards.kb_chose_chain import chose_keyboard_kb
from keyboards.kb_exit_to_chose_chain import exit_to_chose_chain_kb
from keyboards.kb_fallback import fallback_kb
from keyboards.kb_farm_menu import farm_menu_kb

router = Router()

logger = logging.getLogger("farm_start_menu")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == "farm")
@log_callback(logger)
async def farm_menu(callback: types.CallbackQuery, state: FSMContext, db_session: AsyncSession):
    user_id = callback.from_user.id
    farm = await FarmAccsessor(db_session).get_farm_id(user_id)
    if farm:
        await callback.message.edit_text(
            text=FARM_MENU_TEXT, reply_markup=farm_menu_kb()
        )
    else:
        await state.set_state(FarmState.waiting_farm)
        await callback.message.edit_text(
            text=CHOSE_CHAIN_TEXT, reply_markup=chose_keyboard_kb()
        )


@router.callback_query(F.data == "farm_chain_solana")
@log_callback(logger)
async def farm_chain_solana(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chain="solana")
    await callback.message.edit_text(
        text=CREATE_FARM_TEXT, reply_markup=exit_to_chose_chain_kb()
    )


@router.callback_query(F.data == "farm_chain_evm")
@log_callback(logger)
async def farm_chain_evm(callback: types.CallbackQuery):
    await callback.message.edit_text(text=SOON, reply_markup=fallback_kb())


@router.callback_query(F.data == "farm_chain_abstarct")
@log_callback(logger)
async def farm_chain_abstract(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=SOON, reply_markup=fallback_kb())


@router.message(FarmState.waiting_farm)
@log_callback(logger)
async def create_first_farm(
    message: types.Message, state: FSMContext, session: aiohttp.ClientSession,  db_session: AsyncSession
):
    user_id = message.from_user.id
    data = await state.get_data()
    chain = data["chain"]
    new_wallets = message.text.splitlines()
    request = await add_wallet_to_farm(user_id, new_wallets, session, chain, db_session)
    await state.clear()
    await message.answer(text=request, reply_markup=exit_to_chose_chain_kb())
