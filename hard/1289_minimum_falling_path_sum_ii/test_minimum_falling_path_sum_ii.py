import pytest
from minimum_falling_path_sum_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution._min_falling_path_sum(grid) == 13  # 1 → 4 → 8

def test_case_2(solution):
    grid = [
        [7]
    ]
    assert solution._min_falling_path_sum(grid) == 7

def test_case_3(solution):
    grid = [
        [1, 2],
        [3, 4]
    ]
    assert solution._min_falling_path_sum(grid) == 5  # 1 → 4 or 2 → 3

def test_case_4(solution):
    # Random-type example to validate transitions
    grid = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]
    assert solution._min_falling_path_sum(grid) == 12

def test_case_5(solution):
    # Large but structured case for performance
    n = 50
    grid = [[i + j for j in range(n)] for i in range(n)]
    res = solution._min_falling_path_sum(grid)
    assert isinstance(res, int)
