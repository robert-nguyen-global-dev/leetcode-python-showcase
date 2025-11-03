import pytest
from word_ladder_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_basic(solution):
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]
    result = solution._find_ladders(beginWord, endWord, wordList)
    assert sorted(result) == sorted(expected)

def test_case_no_path(solution):
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    assert solution._find_ladders(beginWord, endWord, wordList) == []
