import pytest
from count_of_smaller_numbers_after_self import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [5, 2, 6, 1]
    assert solution._count_smaller_merge_sort(nums) == [2, 1, 1, 0]

def test_case_2(solution):
    nums = [2, 0, 1]
    assert solution._count_smaller_merge_sort(nums) == [2, 0, 0]

def test_case_3(solution):
    nums = [1, 2, 3]
    assert solution._count_smaller_merge_sort(nums) == [0, 0, 0]

def test_case_4(solution):
    nums = [3, 2, 2, 6, 1]
    assert solution._count_smaller_merge_sort(nums) == [3, 1, 1, 1, 0]
