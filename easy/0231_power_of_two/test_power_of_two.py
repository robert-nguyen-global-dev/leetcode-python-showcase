import pytest
from power_of_two import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._is_power_of_two(1) is True

def test_example_case_2(solution):
    assert solution._is_power_of_two(16) is True

def test_not_power_of_two(solution):
    assert solution._is_power_of_two(18) is False

def test_zero(solution):
    assert solution._is_power_of_two(0) is False

def test_negative_number(solution):
    assert solution._is_power_of_two(-8) is False

def test_large_power_of_two(solution):
    assert solution._is_power_of_two(2**30) is True
