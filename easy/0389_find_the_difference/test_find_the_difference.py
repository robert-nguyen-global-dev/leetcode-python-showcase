import pytest
from find_the_difference import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution._find_the_difference("abcd", "abcde") == "e"

def test_example_2(solution):
    assert solution._find_the_difference("", "y") == "y"

def test_example_3(solution):
    assert solution._find_the_difference("a", "aa") == "a"

def test_example_4(solution):
    assert solution._find_the_difference("ae", "aea") == "a"
