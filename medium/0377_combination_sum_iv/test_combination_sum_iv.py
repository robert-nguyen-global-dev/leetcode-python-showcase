import pytest
from combination_sum_iv import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 2, 3]
    target = 4
    assert solution._combination_sum4(nums, target) == 7

def test_case_2(solution):
    nums = [9]
    target = 3
    assert solution._combination_sum4(nums, target) == 0

def test_case_3(solution):
    nums = [2, 4, 6, 8]
    target = 8
    assert solution._combination_sum4(nums, target) == 8  # (2,2,2,2), (2,2,4), (2,4,2), (4,2,2), (2,6), (4,4), (6,2), (8)
