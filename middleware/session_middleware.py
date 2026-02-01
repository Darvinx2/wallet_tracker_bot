from aiogram import BaseMiddleware
from aiohttp import ClientSession


class AiohttpMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.session: ClientSession | None = None

    async def start(self):
        self.session = ClientSession()

    async def stop(self):
        self.session.close()

    async def __call__(self, handler, event, data):
        data["session"] = self.session
        return await handler(event, data)
