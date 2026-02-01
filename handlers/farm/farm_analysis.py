import logging

import aiohttp
from aiogram import F, Router, types

from decorator.log_handlers import log_callback
from infrastructure.farm.analysis_farm import get_answer
from keyboards.kb_exit_to_chose_chain import exit_to_chose_chain_kb

router = Router()

logger = logging.getLogger("farm_analysis")
logger.setLevel(logging.INFO)


@router.callback_query(F.data == "analysis_farm")
@log_callback(logger)
async def analysis_farm(callback: types.CallbackQuery, session=aiohttp.ClientSession):
    user_id = callback.from_user.id
    answer = await get_answer(user_id, session)
    await callback.message.edit_text(text=answer, reply_markup=exit_to_chose_chain_kb())
