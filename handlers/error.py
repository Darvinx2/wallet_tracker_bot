import logging

from aiogram import Router
from aiogram.types import ErrorEvent

from data.text import ERROR

router = Router()

logger = logging.getLogger("error")
logger.setLevel(logging.INFO)


@router.errors()
async def error_handler(event: ErrorEvent) -> None:
    logger.error(f"Error: {event.exception}")
    try:
        await event.update.message.answer(text=ERROR)
    except Exception:
        pass
