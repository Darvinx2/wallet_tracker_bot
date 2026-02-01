from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import BACK_BUTTON


# Временно
def drop_menu_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="back_main_menu")]
        ]
    )

    return keyboard
