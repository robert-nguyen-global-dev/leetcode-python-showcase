import pytest
from next_greater_element import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    assert solution._next_greater_element(nums1, nums2) == [-1,3,-1]

def test_example2(solution):
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    assert solution._next_greater_element(nums1, nums2) == [3,-1]

def test_single_element(solution):
    nums1 = [1]
    nums2 = [1]
    assert solution._next_greater_element(nums1, nums2) == [-1]

def test_increasing_order(solution):
    nums1 = [1,3,5]
    nums2 = [1,2,3,4,5]
    assert solution._next_greater_element(nums1, nums2) == [2,4,-1]

def test_decreasing_order(solution):
    nums1 = [3,2]
    nums2 = [5,4,3,2,1]
    assert solution._next_greater_element(nums1, nums2) == [-1,-1]
