import logging

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from data.text import BALANCE_MENU_TEXT
from decorator.log_handlers import log_callback
from keyboards.kb_balance_menu import balance_menu_kb

router = Router()

logger = logging.getLogger("balance_menu")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == ("balance_menu"))
@log_callback(logger)
async def balance_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.edit_text(
        text=BALANCE_MENU_TEXT, reply_markup=balance_menu_kb()
    )
