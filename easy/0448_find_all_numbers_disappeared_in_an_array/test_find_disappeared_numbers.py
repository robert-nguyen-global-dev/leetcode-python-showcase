import pytest
from find_disappeared_numbers import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    nums = [4,3,2,7,8,2,3,1]
    assert sorted(solution._find_disappeared_numbers(nums)) == [5,6]

def test_example2(solution):
    nums = [1,1]
    assert solution._find_disappeared_numbers(nums) == [2]

def test_no_missing(solution):
    nums = [1,2,3,4,5]
    assert solution._find_disappeared_numbers(nums) == []

def test_all_missing_except_one(solution):
    nums = [2,2,2,2]
    assert solution._find_disappeared_numbers(nums) == [1,3,4]

def test_large_input(solution):
    nums = list(range(1, 21))
    assert solution._find_disappeared_numbers(nums) == []
