import pytest
from longest_increasing_subsequence import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # LIS: [2,3,7,101]

def test_case_2(solution):
    assert solution._length_of_lis([0, 1, 0, 3, 2, 3]) == 4  # LIS: [0,1,2,3]

def test_case_3(solution):
    assert solution._length_of_lis([7, 7, 7, 7]) == 1  # Only one element can form LIS
