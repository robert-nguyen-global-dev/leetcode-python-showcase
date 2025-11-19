import pytest
from furthest_building_you_can_reach import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    assert solution._furthest_building(heights, bricks, ladders) == 4

def test_case_2(solution):
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    assert solution._furthest_building(heights, bricks, ladders) == 7

def test_case_3(solution):
    heights = [1, 2, 3, 4, 5]
    bricks = 0
    ladders = 0
    assert solution._furthest_building(heights, bricks, ladders) == 0
