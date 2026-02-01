from aiogram.fsm.state import State, StatesGroup


class SolanaState(StatesGroup):
    waiting_wallet = State()
