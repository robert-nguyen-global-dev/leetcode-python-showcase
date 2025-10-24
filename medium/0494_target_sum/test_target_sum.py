import pytest
from target_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert solution._find_target_sum_ways(nums, target) == 5

def test_case_2(solution):
    nums = [1]
    target = 1
    assert solution._find_target_sum_ways(nums, target) == 1

def test_case_3(solution):
    nums = [1, 2, 7, 9, 981]
    target = 1000000000
    assert solution._find_target_sum_ways(nums, target) == 0
