import pytest
from longest_palindromic_substring import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._longest_palindromic_substring("babad") in ["bab", "aba"]

def test_example_case_2(solution):
    assert solution._longest_palindromic_substring("cbbd") == "bb"

def test_single_char(solution):
    assert solution._longest_palindromic_substring("a") == "a"

def test_two_same_chars(solution):
    assert solution._longest_palindromic_substring("bb") == "bb"

def test_no_palindrome(solution):
    assert solution._longest_palindromic_substring("abcde")[0] in "abcde"

def test_long_palindrome(solution):
    assert solution._longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_empty_string(solution):
    assert solution._longest_palindromic_substring("") == ""
