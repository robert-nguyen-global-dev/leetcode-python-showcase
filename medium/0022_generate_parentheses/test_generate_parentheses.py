import pytest
from generate_parentheses import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    n = 3
    expected = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert set(solution._generate_parenthesis(n)) == expected

def test_case_2(solution):
    n = 1
    assert solution._generate_parenthesis(n) == ["()"]

def test_case_3(solution):
    n = 2
    expected = {"(())", "()()"}
    assert set(solution._generate_parenthesis(n)) == expected