import pytest
from cherry_pickup_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    grid = [
        [3, 1, 1],
        [2, 5, 1],
        [1, 5, 5],
        [2, 1, 1]
    ]
    assert solution._cherry_pickup(grid) == 24

def test_case_2(solution):
    grid = [
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6]
    ]
    assert solution._cherry_pickup(grid) == 28

def test_case_3(solution):
    grid = [[1, 1], [1, 1]]
    assert solution._cherry_pickup(grid) == 4
