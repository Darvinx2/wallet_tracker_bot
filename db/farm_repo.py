from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from db import db_connection
from models.database_model import Farms, FarmWallets


class FarmRepository():
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

    async def get_farm_wallet(self, user_id: int):
        wallets = await self.session.scalar(
            select(func.array_agg(FarmWallets.wallet)).join(Farms.farm_wallet).where(Farms.user_id == user_id)
        )
        return wallets

    async def delete_farm(self, user_id: int) -> None:
        farm_user_id = await self.session.scalar(
            select(Farms.id).where(Farms.user_id == user_id)
        )
        farm = await self.session.get(Farms, farm_user_id)
        await self.session.delete(farm)
        await self.session.commit()

    async def update_total(self, total: float, user_id: int):
        farm_id = await self.session.scalar(
            select(Farms.id).where(Farms.user_id == user_id)
        )
        farm = await self.session.get(Farms, farm_id)
        farm.total = total
        await self.session.commit()

    async def get_total(self, user_id: int):
        total = await self.session.scalar(
            select(Farms.total).where(Farms.user_id == user_id)
        )
        return total

    async def get_last_date(self, user_id: int):
        created_date = await self.session.scalar(
            select(Farms.created_date).where(Farms.user_id == user_id)
        )
        return created_date
