import pytest
from sum_of_two_integers import Solution


@pytest.fixture
def solution():
    return Solution()


def test_positive_numbers(solution):
    assert solution._bitwise_sum(1, 2) == 3

def test_negative_numbers(solution):
    assert solution._bitwise_sum(-2, -3) == -5

def test_mixed_numbers(solution):
    assert solution._bitwise_sum(-2, 3) == 1

def test_zero(solution):
    assert solution._bitwise_sum(0, 7) == 7
    assert solution._bitwise_sum(5, 0) == 5

def test_large_numbers(solution):
    assert solution._bitwise_sum(123456, 654321) == 777777
