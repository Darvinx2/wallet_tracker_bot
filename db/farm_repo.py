from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from db import db_connection
from models.database_model import Farms, FarmWallets


class FarmAccsessor():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_farm_id(self, user_id: int) -> int:
        farm = await self.session.scalar(
            select(Farms.id).where(Farms.user_id == user_id)
        )

        return farm

    async def insert_farm(self, user_id: int, chain: str, total: float) -> int:
        farm = Farms(user_id=user_id, chain=chain, total=total)
        self.session.add(farm)
        await self.session.commit()
        return farm.id

    async def insert_wallet(self, farm_id: int, chain: str, wallet: str) -> None:
        farm_wallet = FarmWallets(
            farm_id=farm_id,
            chain=chain,
            wallet=wallet,
        )
        self.session.add(farm_wallet)
        await self.session.commit()

    async def get_farm_wallet(user_id: int):
        pass

async def get_farm_wallet(user_id: int):
    return await db_connection.pool.fetchrow(
        "SELECT array_agg(wallet) FROM farm_wallets "
        "JOIN farms "
        "ON farms.id = farm_wallets.farm_id "
        "WHERE user_id = $1;",
        user_id,
    )


async def delete_farm(user_id: int):
    return await db_connection.pool.execute(
        "DELETE FROM farms WHERE user_id = $1", user_id
    )


async def update_total(total: float, user_id: int):
    return await db_connection.pool.execute(
        "UPDATE farms SET total = $1 WHERE user_id = $2", total, user_id
    )


async def get_total(user_id: int):
    return await db_connection.pool.fetchval(
        "SELECT total FROM farms WHERE user_id = $1", user_id
    )


async def get_last_date(user_id: int):
    return await db_connection.pool.fetchval(
        "SELECT created_date FROM farms WHERE user_id = $1", user_id
    )
