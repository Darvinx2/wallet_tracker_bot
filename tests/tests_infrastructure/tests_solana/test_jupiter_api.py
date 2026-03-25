import aiohttp

from infrastructure.solana_api.jupiter_api import JupiterPrice
from models.token_balance import TokenBalance


class TestJupiterPrice:
    async def test_list_tokens_success(self, mock_jupiter_get):
        mock_jupiter_get([
            {
                "id": "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN",
                "name": "Jupiter",
                "symbol": "JUP",
            },
            {
                "holderCount": 853437,
            },
            {
                "createdAt": "2024-06-07T10:56:42.584Z",
                "fdv": 1251807110.62855,
                "mcap": 637825697.675,
                "usdPrice": 0.18237329192588,
            },
        ])

        token_list = [
            TokenBalance(
                balance=100,
                address="JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN",
                name="Jupiter",
            )
        ]

        async with aiohttp.ClientSession() as s:
            jup = JupiterPrice(s, token_list)
            result = await jup.tokens_info()
            assert result == [TokenBalance(
                balance=100,
                name="Jupiter",
                price=0.18237329192588,
            )]

    async def test_list_incorrect_address_name(self, mock_jupiter_get):
        mock_jupiter_get([])

        token_list = [
            TokenBalance(
                balance=100,
                address="QUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN",
                name="Jupiter",
            )
        ]

        async with aiohttp.ClientSession() as s:
            jup = JupiterPrice(s, token_list)
            result = await jup.tokens_info()
            assert result == []

    async def test_list_incorrect_address_len(self, mock_jupiter_get):
        mock_jupiter_get([])

        token_list = [
            TokenBalance(
                balance=100,
                address="So111111111111111111111111111111111111111112",
                name="Jupiter",
            )
        ]

        async with aiohttp.ClientSession() as s:
            jup = JupiterPrice(s, token_list)
            result = await jup.tokens_info()
            assert result == []
