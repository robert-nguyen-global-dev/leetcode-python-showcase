import pytest
from word_break import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    s = "leetcode"
    wordDict = ["leet", "code"]
    assert solution._word_break(s, wordDict) is True

def test_case_2(solution):
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert solution._word_break(s, wordDict) is True

def test_case_3(solution):
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert solution._word_break(s, wordDict) is False
