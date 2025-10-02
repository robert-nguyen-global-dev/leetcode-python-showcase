import pytest
from decode_string import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    s = "3[a]2[bc]"
    assert solution._decodeString(s) == "aaabcbc"

def test_case_2(solution):
    s = "3[a2[c]]"
    assert solution._decodeString(s) == "accaccacc"

def test_case_3(solution):
    s = "2[abc]3[cd]ef"
    assert solution._decodeString(s) == "abcabccdcdcdef"

def test_case_4(solution):
    s = "abc3[cd]xyz"
    assert solution._decodeString(s) == "abccdcdcdxyz"

def test_empty_string(solution):
    s = ""
    assert solution._decodeString(s) == ""
