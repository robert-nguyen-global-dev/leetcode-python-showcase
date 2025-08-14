import pytest
from longest_palindrome import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case(solution):
    assert solution._longest_palindrome("abccccdd") == 7  # "dccaccd"

def test_all_unique_chars(solution):
    assert solution._longest_palindrome("abc") == 1  # Any single char

def test_all_same_char(solution):
    assert solution._longest_palindrome("aaaa") == 4  # Whole string is palindrome

def test_empty_string(solution):
    assert solution._longest_palindrome("") == 0

def test_with_non_ascii(solution):
    assert solution._longest_palindrome("你好你好") == 0  # Only ASCII letters are supported

def test_one_odd_multiple_even(solution):
    assert solution._longest_palindrome("aaabb") == 5  # "baaab"
