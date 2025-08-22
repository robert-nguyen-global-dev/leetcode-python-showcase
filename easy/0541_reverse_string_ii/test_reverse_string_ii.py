import pytest
from reverse_string_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution._reverse_str("abcdefg", 2) == "bacdfeg"

def test_example2(solution):
    assert solution._reverse_str("abcd", 2) == "bacd"

def test_example3(solution):
    assert solution._reverse_str("abcdef", 3) == "cbadef"

def test_single_char(solution):
    assert solution._reverse_str("a", 2) == "a"

def test_k_greater_than_length(solution):
    assert solution._reverse_str("abc", 5) == "cba"

def test_large_case(solution):
    s = "abcdefghijklmnopqrstuvwxyz"
    assert solution._reverse_str(s, 4) == "dcbaefghlkjimnoptsrquvwxzy"
