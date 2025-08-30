import pytest
from container_with_most_water import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._max_container_area([1,8,6,2,5,4,8,3,7]) == 49

def test_example_case_2(solution):
    assert solution._max_container_area([1,1]) == 1

def test_monotonic_increasing(solution):
    assert solution._max_container_area([1,2,3,4,5]) == 6  # lines 2 & 5

def test_monotonic_decreasing(solution):
    assert solution._max_container_area([5,4,3,2,1]) == 6  # lines 1 & 4

def test_equal_heights(solution):
    assert solution._max_container_area([5,5,5,5,5]) == 20

def test_single_line(solution):
    assert solution._max_container_area([5]) == 0

def test_empty_array(solution):
    assert solution._max_container_area([]) == 0
