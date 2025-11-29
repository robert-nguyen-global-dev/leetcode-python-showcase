import pytest
from longest_increasing_path_in_a_matrix import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    assert solution._longest_increasing_path(matrix) == 4

def test_case_2(solution):
    matrix = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    assert solution._longest_increasing_path(matrix) == 4

def test_case_3(solution):
    matrix = [[1]]
    assert solution._longest_increasing_path(matrix) == 1

def test_case_4(solution):
    matrix = [
        [7, 7],
        [7, 7]
    ]
    assert solution._longest_increasing_path(matrix) == 1
