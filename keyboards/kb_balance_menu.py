from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import (BACK_BUTTON, BALANCE_ABSTRACT_BUTTON,
                       BALANCE_EVM_BUTTON, BALANCE_SOLANA_BUTTON, FARM_BUTTON)


# Меню выбора блокчейна
def balance_menu_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=BALANCE_SOLANA_BUTTON, callback_data="balance_solana"
                )
            ],
            [
                InlineKeyboardButton(
                    text=BALANCE_EVM_BUTTON, callback_data="balance_evm"
                )
            ],
            [
                InlineKeyboardButton(
                    text=BALANCE_ABSTRACT_BUTTON, callback_data="balance_abstract"
                )
            ],
            [InlineKeyboardButton(text=FARM_BUTTON, callback_data="farm")],
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="back_main_menu")],
        ]
    )

    return keyboard
