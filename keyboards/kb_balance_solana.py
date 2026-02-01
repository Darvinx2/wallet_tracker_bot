from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import BACK_BUTTON


# Клавиатура Solana кошельков
def balance_solana_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="balance_menu")]
        ]
    )

    return keyboard
