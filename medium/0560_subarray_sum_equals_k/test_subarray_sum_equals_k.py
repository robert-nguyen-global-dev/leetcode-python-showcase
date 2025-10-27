import pytest
from subarray_sum_equals_k import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 1, 1]
    k = 2
    assert solution._subarray_sum(nums, k) == 2


def test_case_2(solution):
    nums = [1, 2, 3]
    k = 3
    assert solution._subarray_sum(nums, k) == 2  # [1,2], [3]


def test_case_3(solution):
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7
    assert solution._subarray_sum(nums, k) == 4
