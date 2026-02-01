import logging
from typing import List

from models.token_balance import TokenBalance

logger = logging.getLogger("formatting")
logger.setLevel(logging.INFO)


async def formatting(tokens: List[TokenBalance]) -> tuple[str, float]:
    output = ""
    total_dollars_on_wallet = 0.0
    for token in tokens:
        if token.total_amount is not None:
            try:
                output += f"{token.name}: {token.balance} ({token.total_amount}$)\n"
                total_dollars_on_wallet += token.total_amount
            except Exception as e:
                logger.warning(f"Data conversion error for {token.name}: {e}")
                continue
    output += f"Total on wallet: {round(total_dollars_on_wallet, 2)}$\n"
    logger.info("Wallet processing completed")
    return output, total_dollars_on_wallet
