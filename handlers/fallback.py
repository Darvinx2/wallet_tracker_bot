import logging

from aiogram import Router
from aiogram.types import Message

from data.text import UNKNOWN_MESSAGE
from decorator.log_handlers import log_callback
from keyboards.kb_fallback import fallback_kb

router = Router()

logger = logging.getLogger("fallback")
logger.setLevel(logging.INFO)


@router.message()
@log_callback(logger)
async def unknown_message(message: Message) -> None:
    await message.answer(text=UNKNOWN_MESSAGE, reply_markup=fallback_kb())
