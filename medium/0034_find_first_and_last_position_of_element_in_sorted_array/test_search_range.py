import pytest
from search_range import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums, target = [5,7,7,8,8,10], 8
    assert solution._search_range(nums, target) == [3, 4]

def test_example_case_2(solution):
    nums, target = [5,7,7,8,8,10], 6
    assert solution._search_range(nums, target) == [-1, -1]

def test_example_case_3(solution):
    nums, target = [], 0
    assert solution._search_range(nums, target) == [-1, -1]

def test_single_element_found(solution):
    nums, target = [1], 1
    assert solution._search_range(nums, target) == [0, 0]

def test_single_element_not_found(solution):
    nums, target = [1], 2
    assert solution._search_range(nums, target) == [-1, -1]
