from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import BACK_BUTTON, EXPAND_FARM_BUTTON, RECREATE_FARM_BUTTON


def edit_farm_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=EXPAND_FARM_BUTTON, callback_data="expand_farm"
                ),
                InlineKeyboardButton(
                    text=RECREATE_FARM_BUTTON, callback_data="recreate_farm"
                ),
            ],
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="farm")],
        ]
    )

    return keyboard
