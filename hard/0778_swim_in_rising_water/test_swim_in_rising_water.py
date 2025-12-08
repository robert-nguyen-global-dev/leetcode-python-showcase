import pytest
from swim_in_rising_water import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    grid = [[0,2],[1,3]]
    assert solution._swim_in_water(grid) == 3

def test_case_2(solution):
    grid = [[0,1,2,3,4],
            [24,23,22,21,5],
            [12,13,14,15,6],
            [11,17,18,19,7],
            [10,9,8,16,20]]
    assert solution._swim_in_water(grid) == 20

def test_case_3(solution):
    grid = [[0]]
    assert solution._swim_in_water(grid) == 0
