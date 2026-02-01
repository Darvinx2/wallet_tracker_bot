import logging

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.text import START_MENU_TEXT
from keyboards.kb_main_menu import main_menu_kb

router = Router()

logger = logging.getLogger("main_menu")
logger.setLevel(logging.INFO)


@router.message(Command("start"))
@router.callback_query(F.data == ("back_main_menu"))
async def start(event: types.Message | types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    if isinstance(event, types.Message):
        logger.info(f"User {event.from_user.id} send command {event.text}")
        await event.answer(text=START_MENU_TEXT, reply_markup=main_menu_kb())
    else:
        logger.info(f"User {event.from_user.id} pressed button with data {event.data}")
        await event.message.edit_text(text=START_MENU_TEXT, reply_markup=main_menu_kb())
