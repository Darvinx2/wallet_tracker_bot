from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import ANALYSIS_FARM_BUTTON, BACK_BUTTON, EDIT_FARM_BUTTON


def farm_menu_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=ANALYSIS_FARM_BUTTON, callback_data="analysis_farm"
                ),
                InlineKeyboardButton(text=EDIT_FARM_BUTTON, callback_data="edit_farm"),
            ],
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="balance_menu")],
        ]
    )

    return keyboard
