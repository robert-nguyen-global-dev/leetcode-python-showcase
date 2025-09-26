import pytest
from find_min_rotated import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [3,4,5,1,2]
    assert solution._find_min(nums) == 1

def test_case_2(solution):
    nums = [4,5,6,7,0,1,2]
    assert solution._find_min(nums) == 0

def test_case_3(solution):
    nums = [11,13,15,17]
    assert solution._find_min(nums) == 11

def test_case_4(solution):
    nums = [2,3,4,5,6,7,1]
    assert solution._find_min(nums) == 1
