import pytest
from merge_sorted_array import Solution


@pytest.fixture
def solution():
    return Solution()
    

def test_case_1(solution):
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution._merge_sorted_array(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

def test_case_2(solution):
    nums1 = [1]
    nums2 = []
    solution._merge_sorted_array(nums1, 1, nums2, 0)
    assert nums1 == [1]

def test_case_3(solution):
    nums1 = [0]
    nums2 = [1]
    solution._merge_sorted_array(nums1, 0, nums2, 1)
    assert nums1 == [1]

def test_case_4(solution):
    nums1 = [2, 0]
    nums2 = [1]
    solution._merge_sorted_array(nums1, 1, nums2, 1)
    assert nums1 == [1, 2]
