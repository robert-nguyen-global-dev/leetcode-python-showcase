import pytest
from maximum_product_subarray import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [2, 3, -2, 4]
    assert solution._max_product_subarray(nums) == 6  # [2,3]

def test_case_2(solution):
    nums = [-2, 0, -1]
    assert solution._max_product_subarray(nums) == 0  # Single 0

def test_case_3(solution):
    nums = [-2, 3, -4]
    assert solution._max_product_subarray(nums) == 24  # [-2,3,-4]
