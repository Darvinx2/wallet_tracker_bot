from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from data.config import DATABASE_URL
from db.sqlalchemy_base import Base


class Database:
    def __init__(self):
        self.engine: AsyncEngine | None = None
        self._db: type[DeclarativeBase] = Base
        self.session: async_sessionmaker | None = None

    async def connect(self):
        url = DATABASE_URL

        self.engine = create_async_engine(
            url=url,
            echo=True,
        )

        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=True,
            expire_on_commit=False,
        )

    async def disconnect(self):
        await self.engine.dispose()
