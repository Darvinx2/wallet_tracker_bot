import logging

from aiogram import F, Router, types

from data.text import SOON
from decorator.log_handlers import log_callback
from keyboards.kb_balance_abstract import balance_abstract_kb

router = Router()

logger = logging.getLogger("balance_abstract")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == ("balance_abstract"))
@log_callback(logger)
async def start(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(text=SOON, reply_markup=balance_abstract_kb())
