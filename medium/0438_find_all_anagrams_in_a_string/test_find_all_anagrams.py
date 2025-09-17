import pytest
from find_all_anagrams import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    s, p = "cbaebabacd", "abc"
    expected = [0, 6]
    assert solution._find_anagrams(s, p) == expected

def test_example_case_2(solution):
    s, p = "abab", "ab"
    expected = [0, 1, 2]
    assert solution._find_anagrams(s, p) == expected

def test_no_anagrams(solution):
    s, p = "abcdefg", "hij"
    assert solution._find_anagrams(s, p) == []

def test_same_length(solution):
    s, p = "abc", "bca"
    assert solution._find_anagrams(s, p) == [0]

def test_single_char(solution):
    s, p = "aaaaa", "a"
    expected = [0, 1, 2, 3, 4]
    assert solution._find_anagrams(s, p) == expected
