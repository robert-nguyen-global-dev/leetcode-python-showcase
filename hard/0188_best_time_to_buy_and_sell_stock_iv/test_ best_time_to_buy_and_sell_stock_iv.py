import pytest
from best_time_to_buy_and_sell_stock_iv import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    k = 2
    prices = [2, 4, 1]
    assert solution._max_profit(k, prices) == 2

def test_case_2(solution):
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    assert solution._max_profit(k, prices) == 7

def test_case_3(solution):
    k = 3
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9]
    assert solution._max_profit(k, prices) == 15

def test_case_4(solution):
    k = 100  # large k → unlimited mode
    prices = [1, 2, 3, 4, 5]
    assert solution._max_profit(k, prices) == 4

def test_case_5(solution):
    k = 1
    prices = [7, 6, 4, 3, 1]
    assert solution._max_profit(k, prices) == 0
