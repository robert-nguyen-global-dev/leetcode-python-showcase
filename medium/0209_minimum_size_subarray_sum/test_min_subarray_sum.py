import pytest
from min_subarray_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    target, nums = 7, [2, 3, 1, 2, 4, 3]
    assert solution._min_sub_array_len(target, nums) == 2  # [4,3]

def test_example_case_2(solution):
    target, nums = 4, [1, 4, 4]
    assert solution._min_sub_array_len(target, nums) == 1  # [4]

def test_example_case_3(solution):
    target, nums = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    assert solution._min_sub_array_len(target, nums) == 0

def test_single_element(solution):
    assert solution._min_sub_array_len(5, [5]) == 1

def test_large_input(solution):
    nums = [1] * 100000
    assert solution._min_sub_array_len(100000, nums) == 100000
