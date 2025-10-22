import pytest
from best_time_to_buy_and_sell_stock_with_cooldown import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    prices = [1, 2, 3, 0, 2]
    assert solution._max_profit_cooldown(prices) == 3  # Buy Day1, Sell Day3, Cooldown, Buy Day4, Sell Day5

def test_case_2(solution):
    prices = [1]
    assert solution._max_profit_cooldown(prices) == 0  # Only one day → no transaction possible

def test_case_3(solution):
    prices = [6, 1, 3, 2, 4, 7]
    assert solution._max_profit_cooldown(prices) == 6  # Buy Day2, Sell Day3, Cooldown, Buy Day4, Sell Day6
