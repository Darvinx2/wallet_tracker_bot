import logging
from typing import List

import aiohttp

from infrastructure.solana_api.base_api import BaseApiClient
from models.token_balance import TokenBalance

logger = logging.getLogger("jupiter_api")
logger.setLevel(logging.INFO)


class JupiterPrice(BaseApiClient):
    def __init__(self, session: aiohttp.ClientSession, token: List[TokenBalance]):
        self.session = session
        self.token = token

    async def tokens_info(self) -> List[TokenBalance]:
        tokens = []
        for info in self.token:
            url = f"https://lite-api.jup.ag/tokens/v2/search?query={str(info.address)}"
            try:
                async with self.session.get(url) as r:
                    data = await self.handler_response(r, "JupiterAPI")
                    if len(data) < 1:
                        logger.warning("Error: empty array received")
                        continue
                    else:
                        for token in data:
                            price = token.get("usdPrice")
                            if price is None:
                                logger.error(f"Price {info.name} is None")
                            else:
                                tokens.append(
                                    TokenBalance(
                                        name=info.name,
                                        balance=info.balance,
                                        price=price,
                                    )
                                )
            except aiohttp.ClientConnectionError as e:
                logger.error(f"Не удалось подключиться к JupiterAPI: {e}")
                raise Exception(
                    "Не удалось подключиться к JupiterAPI, проверьте подключение к интернету"
                )
            except aiohttp.ClientError as e:
                logger.error(f"Не удалось подключиться к JupiterAPI: {e}")
                raise Exception("JupiterAPI не отвечает")

        return tokens
