import pytest
from path_with_minimum_effort import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    assert solution._minimum_effort_path(heights) == 2

def test_case_2(solution):
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    assert solution._minimum_effort_path(heights) == 1

def test_case_3(solution):
    heights = [[1,2,1,1,1],
               [1,2,1,2,1],
               [1,2,1,2,1],
               [1,2,1,2,1],
               [1,1,1,2,1]]
    assert solution._minimum_effort_path(heights) == 0

def test_case_4(solution):
    heights = [[8,3,5],[3,2,1],[4,6,7]]
    assert solution._minimum_effort_path(heights) == 5

def test_case_5(solution):
    # Single cell
    heights = [[10]]
    assert solution._minimum_effort_path(heights) == 0
