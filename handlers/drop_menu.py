import logging

from aiogram import F, Router, types

from data.text import SOON
from decorator.log_handlers import log_callback
from keyboards.kb_drop_menu import drop_menu_kb

router = Router()

logger = logging.getLogger("drop_menu")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == ("drop_menu"))
@log_callback(logger)
async def drop_menu(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=SOON, reply_markup=drop_menu_kb())
