import pytest
from power_of_three import Solution


@pytest.fixture
def solution():
    return Solution()


def test_power_of_three_true(solution):
    assert solution._is_power_of_three(27) is True

def test_power_of_three_false(solution):
    assert solution._is_power_of_three(0) is False

def test_power_of_three_one(solution):
    assert solution._is_power_of_three(1) is True  # 3^0

def test_power_of_three_negative(solution):
    assert solution._is_power_of_three(-3) is False

def test_large_false(solution):
    assert solution._is_power_of_three(45) is False
