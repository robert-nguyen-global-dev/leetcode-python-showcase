import pytest
from sqrt_x import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._binary_search_sqrt(4) == 2

def test_example_case_2(solution):
    assert solution._binary_search_sqrt(8) == 2

def test_zero(solution):
    assert solution._binary_search_sqrt(0) == 0

def test_one(solution):
    assert solution._binary_search_sqrt(1) == 1

def test_large_number(solution):
    assert solution._binary_search_sqrt(10**6) == 1000
