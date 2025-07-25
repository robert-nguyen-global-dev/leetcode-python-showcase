import pytest
from single_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution._single_number([2, 2, 1]) == 1

def test_example_2(solution):
    assert solution._single_number([4, 1, 2, 1, 2]) == 4

def test_single_element(solution):
    assert solution._single_number([99]) == 99

def test_large_numbers(solution):
    assert solution._single_number([10**9, 10**9, 42]) == 42

def test_negative_numbers(solution):
    assert solution._single_number([-1, -1, -2]) == -2

def test_mixed_positive_negative(solution):
    assert solution._single_number([-1, 2, 2, -1, 3]) == 3
