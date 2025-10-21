import pytest
from house_robber_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [2, 3, 2]
    assert solution._rob_circular(nums) == 3  # Rob middle house only

def test_case_2(solution):
    nums = [1, 2, 3, 1]
    assert solution._rob_circular(nums) == 4  # Rob house 2 and 4

def test_case_3(solution):
    nums = [1, 2, 3]
    assert solution._rob_circular(nums) == 3  # Rob last house only
