import pytest
from min_cost_to_connect_all_points import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert solution._min_cost_connect_points(points) == 20

def test_case_2(solution):
    points = [[3,12],[-2,5],[-4,1]]
    assert solution._min_cost_connect_points(points) == 18

def test_case_3(solution):
    points = [[0,0],[1,1],[1,0],[-1,1]]
    assert solution._min_cost_connect_points(points) == 4
