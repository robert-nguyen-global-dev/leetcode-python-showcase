import pytest
from sliding_puzzle import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    board = [[1,2,3],[4,0,5]]
    assert solution._sliding_puzzle(board) == 1

def test_case_2(solution):
    board = [[1,2,3],[5,4,0]]
    assert solution._sliding_puzzle(board) == -1

def test_case_3(solution):
    board = [[4,1,2],[5,0,3]]
    assert solution._sliding_puzzle(board) == 5

def test_case_4(solution):
    board = [[3,2,4],[1,5,0]]
    assert solution._sliding_puzzle(board) == 14
