import pytest
from coin_change_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    amount = 5
    coins = [1, 2, 5]
    assert solution._coin_change_ways(amount, coins) == 4
    # 4 cách: (5), (2+2+1), (2+1+1+1), (1+1+1+1+1)

def test_case_2(solution):
    amount = 3
    coins = [2]
    assert solution._coin_change_ways(amount, coins) == 0  # Không thể tạo ra 3

def test_case_3(solution):
    amount = 10
    coins = [10]
    assert solution._coin_change_ways(amount, coins) == 1  # Dùng 1 đồng 10
