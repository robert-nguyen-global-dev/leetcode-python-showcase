import pytest
from coin_change import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    coins = [1, 2, 5]
    amount = 11
    assert solution._coin_change(coins, amount) == 3  # 5 + 5 + 1

def test_case_2(solution):
    coins = [2]
    amount = 3
    assert solution._coin_change(coins, amount) == -1  # Impossible

def test_case_3(solution):
    coins = [1]
    amount = 0
    assert solution._coin_change(coins, amount) == 0  # No coins needed
