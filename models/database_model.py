import datetime

from sqlalchemy import BIGINT, REAL, CheckConstraint, func, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.sqlalchemy_base import Base


class Farms(Base):
    __tablename__ = "farms"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT, nullable=False, unique=True)
    chain: Mapped[str] = mapped_column(String(12), nullable=False)
    total: Mapped[float] = mapped_column(REAL, nullable=False, server_default="0")
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    __table_args__ = (
        CheckConstraint(
            "chain in ('solana', 'evm', 'abstract')",
            name="check_chain"),
    )

    farm_wallet = relationship("FarmWallets", back_populates="farm", cascade="all, delete-orphan")

class FarmWallets(Base):
    __tablename__ = "farm_wallets"
    id: Mapped[int] = mapped_column(primary_key=True)
    farm_id: Mapped[int] = mapped_column(ForeignKey("farms.id", ondelete="CASCADE"), nullable=False)
    chain: Mapped[str] = mapped_column(String(12), nullable=False)
    wallet: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    __table_args__ = (
        CheckConstraint(
            "chain in ('solana', 'evm', 'abstract')",
            name="check_chain"),
        )

    farm = relationship("Farms", back_populates="farm_wallet")
