import pytest
from longest_increasing_subsequence_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 5, 4, 6, 2, 3]
    k = 2
    assert solution._length_of_lis(nums, k) == 3

def test_case_2(solution):
    nums = [1, 2, 3, 4]
    k = 3
    assert solution._length_of_lis(nums, k) == 4

def test_case_3(solution):
    nums = [5, 3, 4, 6, 2, 1]
    k = 1
    assert solution._length_of_lis(nums, k) == 2
