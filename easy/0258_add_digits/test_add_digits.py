import pytest
from add_digits import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_digit(solution):
    assert solution._add_digits(5) == 5

def test_example_case(solution):
    assert solution._add_digits(38) == 2

def test_zero_case(solution):
    assert solution._add_digits(0) == 0

def test_multiple_levels(solution):
    assert solution._add_digits(9999) == 9

def test_large_number(solution):
    assert solution._add_digits(123456) == 3
