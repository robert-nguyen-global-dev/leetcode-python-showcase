import pytest
from build_a_matrix_with_conditions import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    k = 3
    row = [[1, 2], [3, 2]]
    col = [[2, 1], [3, 2]]

    result = solution._build_matrix(k, row, col)

    flat = [x for r in result for x in r if x != 0]
    assert sorted(flat) == [1, 2, 3]

def test_case_2(solution):
    # Impossible due to cycle
    k = 3
    row = [[1, 2], [2, 1]]
    col = []
    assert solution._build_matrix(k, row, col) == []

def test_case_3(solution):
    k = 4
    row = [[1, 2], [3, 4]]
    col = [[2, 3]]
    mat = solution._build_matrix(k, row, col)

    # Ensure all numbers appear exactly once
    flat = [x for r in mat for x in r if x != 0]
    assert sorted(flat) == [1, 2, 3, 4]

def test_case_4(solution):
    # Large no-conflict scenario
    k = 5
    row = []
    col = []
    mat = solution._build_matrix(k, row, col)

    # Should simply place numbers arbitrarily but valid (no zeros)
    assert len(mat) == 5
    assert len(mat[0]) == 5
