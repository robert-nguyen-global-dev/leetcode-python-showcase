import pytest
from longest_substring_without_repeating import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    assert solution._length_of_longest_substring("abcabcbb") == 3  # "abc"

def test_example_case_2(solution):
    assert solution._length_of_longest_substring("bbbbb") == 1  # "b"

def test_example_case_3(solution):
    assert solution._length_of_longest_substring("pwwkew") == 3  # "wke"

def test_empty_string(solution):
    assert solution._length_of_longest_substring("") == 0

def test_single_char(solution):
    assert solution._length_of_longest_substring("a") == 1

def test_all_unique_chars(solution):
    assert solution._length_of_longest_substring("abcdef") == 6  # entire string

def test_repeated_chars_late(solution):
    assert solution._length_of_longest_substring("dvdf") == 3  # "vdf"
