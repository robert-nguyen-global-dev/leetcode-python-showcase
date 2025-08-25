import pytest
from binary_search import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    # Input: nums = [-1,0,3,5,9,12], target = 9 → Output: 4
    assert solution._binary_search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_example2(solution):
    # Input: nums = [-1,0,3,5,9,12], target = 2 → Output: -1
    assert solution._binary_search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_single_element_found(solution):
    # Input: nums = [5], target = 5 → Output: 0
    assert solution._binary_search([5], 5) == 0

def test_single_element_not_found(solution):
    # Input: nums = [5], target = 3 → Output: -1
    assert solution._binary_search([5], 3) == -1

def test_empty_array(solution):
    # Input: nums = [], target = 1 → Output: -1
    assert solution._binary_search([], 1) == -1

def test_target_first_element(solution):
    # Input: nums = [2,3,4,5,6], target = 2 → Output: 0
    assert solution._binary_search([2, 3, 4, 5, 6], 2) == 0

def test_target_last_element(solution):
    # Input: nums = [1,3,5,7], target = 7 → Output: 3
    assert solution._binary_search([1, 3, 5, 7], 7) == 3
