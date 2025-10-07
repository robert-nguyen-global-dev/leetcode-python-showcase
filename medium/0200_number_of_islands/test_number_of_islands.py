import pytest
from number_of_islands import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution._num_islands(grid) == 1


def test_case_2(solution):
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert solution._num_islands(grid) == 3


def test_case_3(solution):
    grid = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert solution._num_islands(grid) == 0
