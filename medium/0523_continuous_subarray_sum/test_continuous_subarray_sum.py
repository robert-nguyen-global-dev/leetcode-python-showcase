import pytest
from continuous_subarray_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [23, 2, 4, 6, 7]
    k = 6
    assert solution._check_subarray_sum(nums, k) is True  # subarray [2,4] sum=6


def test_case_2(solution):
    nums = [23, 2, 6, 4, 7]
    k = 13
    assert solution._check_subarray_sum(nums, k) is False


def test_case_3(solution):
    nums = [5, 0, 0]
    k = 3
    assert solution._check_subarray_sum(nums, k) is True  # [0,0] sum=0 divisible by 3
