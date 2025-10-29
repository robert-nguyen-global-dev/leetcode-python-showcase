import pytest
from product_of_array_except_self import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 2, 3, 4]
    assert solution._product_except_self(nums) == [24, 12, 8, 6]

def test_case_2(solution):
    nums = [-1, 1, 0, -3, 3]
    assert solution._product_except_self(nums) == [0, 0, 9, 0, 0]

def test_case_3(solution):
    nums = [2, 3, 4, 5]
    assert solution._product_except_self(nums) == [60, 40, 30, 24]
