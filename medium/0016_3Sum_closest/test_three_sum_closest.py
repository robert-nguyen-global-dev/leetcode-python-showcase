import pytest
from three_sum_closest import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [-1, 2, 1, -4]
    target = 1
    assert solution._three_sum_closest(nums, target) == 2

def test_exact_match(solution):
    nums = [0, 1, 2]
    target = 3
    assert solution._three_sum_closest(nums, target) == 3

def test_negative_numbers(solution):
    nums = [-3, -2, -5, 3, -4]
    target = -1
    assert solution._three_sum_closest(nums, target) == -2

def test_large_input(solution):
    nums = [1, 1, 1, 1]
    target = 0
    assert solution._three_sum_closest(nums, target) == 3
