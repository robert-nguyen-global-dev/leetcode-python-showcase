import pytest
from word_search import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    assert solution._exist(board, word) == True

def test_case_2(solution):
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "SEE"
    assert solution._exist(board, word) == True

def test_case_3(solution):
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCB"
    assert solution._exist(board, word) == False

def test_single_letter(solution):
    board = [["A"]]
    word = "A"
    assert solution._exist(board, word) == True
