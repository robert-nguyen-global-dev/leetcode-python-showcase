import pytest
from happy_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_happy_number_true(solution):
    assert solution._is_happy(19) is True

def test_happy_number_false(solution):
    assert solution._is_happy(2) is False

def test_single_digit_happy(solution):
    assert solution._is_happy(1) is True

def test_single_digit_unhappy(solution):
    assert solution._is_happy(4) is False

def test_large_happy_number(solution):
    assert solution._is_happy(100000) is True

def test_large_unhappy_number(solution):
    assert solution._is_happy(9999) is False
