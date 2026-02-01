from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.text import (BACK_BUTTON, FARM_ABSTRACT_BUTTON, FARM_EVM_BUTTON,
                       FARM_SOLANA_BUTTON)


def chose_keyboard_kb():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=FARM_SOLANA_BUTTON, callback_data="farm_chain_solana"
                ),
                InlineKeyboardButton(
                    text=FARM_EVM_BUTTON, callback_data="farm_chain_evm"
                ),
                InlineKeyboardButton(
                    text=FARM_ABSTRACT_BUTTON, callback_data="farm_chain_abstract"
                ),
            ],
            [InlineKeyboardButton(text=BACK_BUTTON, callback_data="balance_menu")],
        ]
    )

    return keyboard
