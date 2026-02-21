from aiogram import BaseMiddleware
from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from db.database import session


class AiohttpMiddleware(BaseMiddleware):
    def __init__(self, session_maker: async_sessionmaker):
        super().__init__()
        self.session: ClientSession | None = None
        self.session_maker = session_maker

    async def start(self):
        self.session = ClientSession()

    async def stop(self):
        await self.session.close()

    async def __call__(self, handler, event, data):
        data["session"] = self.session

        async with self.session_maker() as db_session:
            data["db_session"] = db_session

            return await handler(event, data)
