from aiogram.fsm.state import State, StatesGroup


class FarmState(StatesGroup):
    waiting_farm = State()
    waiting_update_wallets = State()
