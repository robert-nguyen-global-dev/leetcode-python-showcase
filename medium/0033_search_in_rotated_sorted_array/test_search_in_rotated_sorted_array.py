import pytest
from search_in_rotated_sorted_array import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [4,5,6,7,0,1,2]
    target = 0
    assert solution._search_rotated_sorted_array(nums, target) == 4

def test_example_case_2(solution):
    nums = [4,5,6,7,0,1,2]
    target = 3
    assert solution._search_rotated_sorted_array(nums, target) == -1

def test_no_rotation(solution):
    nums = [1,2,3,4,5,6,7]
    target = 3
    assert solution._search_rotated_sorted_array(nums, target) == 2

def test_single_element_found(solution):
    nums = [1]
    target = 1
    assert solution._search_rotated_sorted_array(nums, target) == 0

def test_single_element_not_found(solution):
    nums = [1]
    target = 0
    assert solution._search_rotated_sorted_array(nums, target) == -1

def test_rotation_at_end(solution):
    nums = [6,7,8,1,2,3,4,5]
    target = 3
    assert solution._search_rotated_sorted_array(nums, target) == 5
