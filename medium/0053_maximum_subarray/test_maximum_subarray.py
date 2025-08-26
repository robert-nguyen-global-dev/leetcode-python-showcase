import pytest
from maximum_subarray import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    # Input: [-2,1,-3,4,-1,2,1,-5,4]
    # Max subarray: [4,-1,2,1] => sum = 6
    assert solution._max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_example2(solution):
    # Input: [1]
    assert solution._max_subarray([1]) == 1

def test_example3(solution):
    # Input: [5,4,-1,7,8]
    assert solution._max_subarray([5,4,-1,7,8]) == 23

def test_all_negative(solution):
    # Input: [-3,-2,-1]
    # Best subarray: [-1]
    assert solution._max_subarray([-3,-2,-1]) == -1

def test_mixed_small_case(solution):
    # Input: [1,2,3,-2,5]
    # Best subarray: [1,2,3,-2,5] => sum = 9
    assert solution._max_subarray([1,2,3,-2,5]) == 9
