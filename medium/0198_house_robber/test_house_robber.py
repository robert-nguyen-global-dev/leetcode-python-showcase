import pytest
from house_robber import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 2, 3, 1]
    assert solution._rob_house(nums) == 4  # Rob house 1 and 3

def test_case_2(solution):
    nums = [2, 7, 9, 3, 1]
    assert solution._rob_house(nums) == 12  # Rob houses 2 and 4

def test_case_3(solution):
    nums = [2]
    assert solution._rob_house(nums) == 2  # Only one house
