import pytest
from word_search_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_basic(solution):
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(solution._find_words(board, words)) == sorted(["oath", "eat"])

def test_case_no_match(solution):
    board = [["a", "b"], ["c", "d"]]
    words = ["efg", "hi"]
    assert solution._find_words(board, words) == []

def test_case_single_word(solution):
    board = [["a", "b"], ["c", "d"]]
    words = ["abcd"]
    assert solution._find_words(board, words) == []
