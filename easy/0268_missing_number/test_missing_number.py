import pytest
from missing_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_missing_middle(solution):
    assert solution._missing_number([3, 0, 1]) == 2

def test_missing_first(solution):
    assert solution._missing_number([1, 2, 3]) == 0

def test_missing_last(solution):
    assert solution._missing_number([0, 1, 2]) == 3

def test_large_input(solution):
    nums = list(range(10000))
    nums.remove(4567)
    assert solution._missing_number(nums) == 4567

def test_only_one_missing(solution):
    assert solution._missing_number([0]) == 1
