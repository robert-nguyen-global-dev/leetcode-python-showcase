import pytest
from fizz_buzz import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution._fizz_buzz(3) == ["1", "2", "Fizz"]

def test_example2(solution):
    assert solution._fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

def test_example3(solution):
    assert solution._fizz_buzz(15)[-1] == "FizzBuzz"

def test_no_fizzbuzz(solution):
    assert solution._fizz_buzz(2) == ["1", "2"]

def test_large_n(solution):
    result = solution._fizz_buzz(20)
    assert result[14] == "FizzBuzz"  # 15th element (i=15)
    assert result[2] == "Fizz"       # i=3
    assert result[4] == "Buzz"       # i=5
