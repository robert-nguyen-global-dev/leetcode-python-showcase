import pytest
from word_ladder import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_basic(solution):
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert solution._ladder_length(beginWord, endWord, wordList) == 5

def test_case_no_path(solution):
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    assert solution._ladder_length(beginWord, endWord, wordList) == 0

def test_case_one_step(solution):
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    assert solution._ladder_length(beginWord, endWord, wordList) == 2
