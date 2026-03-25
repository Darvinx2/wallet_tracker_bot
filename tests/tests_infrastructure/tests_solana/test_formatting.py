import pytest

from infrastructure.solana_api.formatting import formatting
from models.token_balance import TokenBalance


class TestFormattingSolana:
    async def test_success(self, current_token_balance):
        result, total_dollars = await formatting(current_token_balance)
        assert result == ('Jupiter: 33.33 (33.33$)\n'
                          'Pudgy Penguins: 10000.0 (50.0$)\n'
                          f'Total on wallet: {33.33 * 1 + 10000.0 * 0.005}$\n')
        assert total_dollars == 33.33 * 1 + 10000.0 * 0.005

    async def test_token_count_zero(self, token_balance_token_count_zero):
        result, total_dollars = await formatting(token_balance_token_count_zero)
        assert result == 'Total on wallet: 0.0$\n'
        assert total_dollars == 0.0

    async def test_small_token_count(self, token_balance_small_token_count):
        result, total_dollars = await formatting(token_balance_small_token_count)
        assert result == 'Total on wallet: 0.0$\n'
        assert total_dollars == 0.0

    async def test_empty_list(self, token_balance_empty_list):
        result, total_dollars = await formatting(token_balance_empty_list)
        assert result == 'Total on wallet: 0.0$\n'
        assert total_dollars == 0.0

    async def test_empty_class(self, token_balance_empty_class):
        result, total_dollars = await formatting(token_balance_empty_class)
        assert result == 'Total on wallet: 0.0$\n'
        assert total_dollars == 0.0

    async def test_negative_price(self, token_balance_negative_price):
        result, total_dollars = await formatting(token_balance_negative_price)
        assert result == 'Total on wallet: 0.0$\n'
        assert total_dollars == 0.0
