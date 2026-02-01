from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import BALANCE_MENU_BUTTON, DROP_MENU_BUTTON


# Основное меню пользователя
def main_menu_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=BALANCE_MENU_BUTTON, callback_data="balance_menu"
                )
            ],
            [InlineKeyboardButton(text=DROP_MENU_BUTTON, callback_data="drop_menu")],
        ]
    )

    return keyboard
