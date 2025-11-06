import pytest
from sliding_window_maximum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_basic(solution):
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    assert solution._max_sliding_window(nums, k) == [3,3,5,5,6,7]

def test_case_single_window(solution):
    nums = [1, -1]
    k = 1
    assert solution._max_sliding_window(nums, k) == [1, -1]

def test_case_small_array(solution):
    nums = [9, 11]
    k = 2
    assert solution._max_sliding_window(nums, k) == [11]

def test_case_increasing(solution):
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert solution._max_sliding_window(nums, k) == [2, 3, 4, 5]
