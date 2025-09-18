import pytest
from permutation_in_string import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._check_inclusion("ab", "eidbaooo") is True  # "ba" exists

def test_example_case_2(solution):
    assert solution._check_inclusion("ab", "eidboaoo") is False

def test_exact_match(solution):
    assert solution._check_inclusion("abc", "cba") is True

def test_longer_s1_than_s2(solution):
    assert solution._check_inclusion("abcd", "abc") is False

def test_repeated_chars(solution):
    assert solution._check_inclusion("aab", "eidbaaoo") is True
