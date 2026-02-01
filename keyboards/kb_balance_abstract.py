from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import BACK_BUTTON


# Временная клавиатура проверки Abstract баланса
def balance_abstract_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="balance_menu")],
        ]
    )

    return keyboard
