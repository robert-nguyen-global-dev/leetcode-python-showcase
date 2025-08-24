import pytest
from valid_palindrome_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    # Input: "aba"
    assert solution._valid_palindrome("aba") is True

def test_example2(solution):
    # Input: "abca" → Remove 'c' → "aba"
    assert solution._valid_palindrome("abca") is True

def test_example3(solution):
    # Input: "abc" → Cannot be palindrome by removing only 1 char
    assert solution._valid_palindrome("abc") is False

def test_single_char(solution):
    # Any single character is palindrome
    assert solution._valid_palindrome("a") is True

def test_empty_string(solution):
    # Empty string is palindrome
    assert solution._valid_palindrome("") is True

def test_complex_case(solution):
    # Input: "deeee" → Remove 'd' → "eeee"
    assert solution._valid_palindrome("deeee") is True
