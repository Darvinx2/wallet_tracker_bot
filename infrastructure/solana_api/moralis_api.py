import logging
from typing import Any, List, Mapping

import aiohttp

from data.config import MORALIS_API_TOKEN
from infrastructure.solana_api.base_api import BaseApiClient
from models.token_balance import TokenBalance

logger = logging.getLogger("moralis_api")
logger.setLevel(logging.INFO)


class MoralisPortfolio(BaseApiClient):
    def __init__(self, session: aiohttp.ClientSession, wallet: str) -> None:
        self.wallet = wallet
        self.session = session

    async def get_portfolio(self) -> Mapping[str, Any]:
        url = f"https://solana-gateway.moralis.io/account/mainnet/{self.wallet}/portfolio?nftMetadata=false&mediaItems=false&excludeSpam=true"

        headers = {"Accept": "application/json", "X-API-Key": MORALIS_API_TOKEN}

        try:
            async with self.session.get(url, headers=headers) as r:
                return await self.handler_response(r, "MoralisAPI")
        except aiohttp.ClientConnectionError as e:
            logger.error(f"Не удалось подключиться к MoralisAPI: {e}")
            raise Exception(
                "Не удалось подключиться к MoralisAPI, проверьте подключение к интернету"
            )
        except aiohttp.ClientError as e:
            logger.error(f"Не удалось подключиться к MoralisAPI: {e}")
            raise Exception("MoralisAPI не отвечает")

    async def get_tokens(self) -> List[TokenBalance]:
        data = await self.get_portfolio()  # получаем json данные о токенах
        solana_address = "So11111111111111111111111111111111111111112"
        solana_balance = str(data.get("nativeBalance", {}).get("solana", "0"))
        solana = TokenBalance(
            "Solana", solana_balance, solana_address
        )  # получаем массив с данными Solana
        tokens = [
            TokenBalance(
                name=token.get("name"),
                balance=token.get("amount"),
                address=token.get("mint"),
            )
            for token in data.get("tokens", [])
        ]  # получаем массив [название, колличество, адрес] для дальнейшей его обработки
        tokens.append(solana)
        return tokens
