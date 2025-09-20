import pytest
from find_peak_element import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [1, 2, 3, 1]
    assert solution._find_peak_element(nums) == 2  # nums[2] = 3 is a peak

def test_example_case_2(solution):
    nums = [1, 2, 1, 3, 5, 6, 4]
    peak_index = solution._find_peak_element(nums)
    assert nums[peak_index] in (2, 6)  # both are valid peaks

def test_single_element(solution):
    assert solution._find_peak_element([1]) == 0

def test_two_elements(solution):
    nums = [1, 2]
    assert solution._find_peak_element(nums) == 1

def test_decreasing_array(solution):
    nums = [5, 4, 3, 2, 1]
    assert solution._find_peak_element(nums) == 0
