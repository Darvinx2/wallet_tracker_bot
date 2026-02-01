import logging
from dataclasses import dataclass
from typing import Optional, Union

logger = logging.getLogger("dataclass")
logger.setLevel(logging.INFO)


@dataclass
class TokenBalance:
    name: str = ""
    balance: float = 0
    address: Optional[str] = None
    price: Optional[float] = None

    def __post_init__(self):
        if isinstance(self.balance, str):
            self.balance = float(self.balance)
        if isinstance(self.price, str):
            self.price = float(self.price)

    @property
    def total_amount(self) -> Union[float, None]:
        try:
            if isinstance(self.price, (int, float)) and isinstance(
                self.balance, (int, float)
            ):
                total_amount = round(self.price * self.balance, 2)
                min_balance = 1
                if total_amount <= min_balance:
                    return None
                else:
                    return total_amount
            else:
                return None
        except Exception:
            logger.error(f"Error calculating: {Exception}")
            raise f"Error calculating: {Exception}"
