import pytest
from valid_palindrome import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True

def test_example_2(solution):
    assert solution.isPalindrome("race a car") is False

def test_empty_string(solution):
    assert solution.isPalindrome("") is True

def test_only_symbols(solution):
    assert solution.isPalindrome("!!@@##$$") is True

def test_numeric_palindrome(solution):
    assert solution.isPalindrome("12321") is True

def test_mixed_case_palindrome(solution):
    assert solution.isPalindrome("Noon") is True
