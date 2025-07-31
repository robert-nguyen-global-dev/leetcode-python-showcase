import pytest
from valid_anagram import Solution


@pytest.fixture
def solution():
    return Solution()


def test_anagram_true(solution):
    assert solution._is_anagram("anagram", "nagaram") is True

def test_anagram_false(solution):
    assert solution._is_anagram("rat", "car") is False

def test_different_lengths(solution):
    assert solution._is_anagram("abc", "ab") is False

def test_empty_strings(solution):
    assert solution._is_anagram("", "") is True

def test_unicode_characters(solution):
    assert solution._is_anagram("你好", "好你") is False  # method only supports ASCII lowercase
