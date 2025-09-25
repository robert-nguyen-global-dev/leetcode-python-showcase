import pytest
from search_matrix import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert solution._search_matrix(matrix, 3) is True

def test_case_2(solution):
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert solution._search_matrix(matrix, 13) is False

def test_case_3(solution):
    matrix = [[1]]
    assert solution._search_matrix(matrix, 1) is True

def test_case_4(solution):
    matrix = [[1]]
    assert solution._search_matrix(matrix, 2) is False
