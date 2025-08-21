import pytest
from fibonacci_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution._fib(2) == 1

def test_example2(solution):
    assert solution._fib(3) == 2

def test_example3(solution):
    assert solution._fib(4) == 3

def test_base_case_zero(solution):
    assert solution._fib(0) == 0

def test_base_case_one(solution):
    assert solution._fib(1) == 1

def test_large_n(solution):
    assert solution._fib(30) == 832040
