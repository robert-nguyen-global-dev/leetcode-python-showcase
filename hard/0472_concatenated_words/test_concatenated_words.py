import pytest
from concatenated_words import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic(solution):
    words = ["cat", "cats", "dog", "catsdog"]
    assert solution._find_all_concatenated_words(words) == ["catsdog"]

def test_multiple(solution):
    words = ["cat", "dog", "catdog", "dogcat", "catdogcat"]
    output = solution._find_all_concatenated_words(words)
    assert sorted(output) == ["catdog", "catdogcat", "dogcat"]

def test_empty(solution):
    assert solution._find_all_concatenated_words([]) == []

def test_repeat_words(solution):
    words = ["a", "aa", "aaa", "aaaa"]
    result = solution._find_all_concatenated_words(words)
    assert sorted(result) == ["aa", "aaa", "aaaa"]

def test_no_concatenated(solution):
    words = ["hello", "world", "leetcode"]
    assert solution._find_all_concatenated_words(words) == []
