import pytest
from ransom_note import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_cases(solution):
    assert solution._can_construct("a", "b") is False
    assert solution._can_construct("aa", "ab") is False
    assert solution._can_construct("aa", "aab") is True

def test_empty_ransom(solution):
    assert solution._can_construct("", "abc") is True

def test_empty_magazine(solution):
    assert solution._can_construct("a", "") is False

def test_identical_strings(solution):
    assert solution._can_construct("abc", "abc") is True

def test_repeated_chars(solution):
    assert solution._can_construct("aaa", "aaaaa") is True
    assert solution._can_construct("aaaa", "aaa") is False