import aiohttp
import pytest

from models.token_balance import TokenBalance


class MockResponse:
    def __init__(self, payload):
        self.payload = payload

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def json(self):
        return self.payload


@pytest.fixture
def current_token_balance():
    return [
        TokenBalance("Jupiter", 33.33, "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", 1),
        TokenBalance("Pudgy Penguins", 10000.00, "2zMMhcVQEXDtdE6vsFS7S7D5oUodfJHE8vd1gnBouauv", 0.005),
        TokenBalance("Grass", 55.55, "Grass7B4RdKfBCjTKgSqnXkqjwiGvQyFbuSCUJr3XXjs", 0.003111),
    ]


@pytest.fixture
def token_balance_token_count_zero():
    return [
        TokenBalance("Jupiter", 0, "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", 0.1718),
    ]


@pytest.fixture
def token_balance_small_token_count():
    return [
        TokenBalance("Jupiter", 9.9, "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", 0.1),
    ]


@pytest.fixture
def token_balance_empty_list():
    return []


@pytest.fixture
def token_balance_empty_class():
    return [
        TokenBalance()
    ]


@pytest.fixture
def token_balance_negative_price():
    return [
        TokenBalance("Jupiter", -9.9, "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", 0.1),
    ]


@pytest.fixture
def mock_jupiter_get(monkeypatch):
    def mock_(payload):
        def mock_get(*args, **kwargs):
            return MockResponse(payload)

        monkeypatch.setattr(aiohttp.ClientSession, "get", mock_get)
    return mock_
