import pytest
from island_perimeter import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    assert solution._island_perimeter(grid) == 16

def test_single_cell(solution):
    grid = [[1]]
    assert solution._island_perimeter(grid) == 4

def test_row_of_land(solution):
    grid = [[1,1,1]]
    assert solution._island_perimeter(grid) == 8

def test_column_of_land(solution):
    grid = [[1],[1],[1]]
    assert solution._island_perimeter(grid) == 8

def test_no_land(solution):
    grid = [[0,0],[0,0]]
    assert solution._island_perimeter(grid) == 0
