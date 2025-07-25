import pytest
from best_time_to_buy_and_sell_stock import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case(solution):
    assert solution._max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_no_profit(solution):
    assert solution._max_profit([7, 6, 4, 3, 1]) == 0

def test_single_price(solution):
    assert solution._max_profit([5]) == 0

def test_empty_list(solution):
    assert solution._max_profit([]) == 0

def test_constant_prices(solution):
    assert solution._max_profit([3, 3, 3, 3]) == 0

def test_early_peak(solution):
    assert solution._max_profit([9, 1, 5, 6, 2]) == 5
