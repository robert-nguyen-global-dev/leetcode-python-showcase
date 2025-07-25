import pytest
from valid_parentheses import Solution


@pytest.fixture
def solution():
    return Solution()
    

def test_valid_cases(solution):
    assert solution._is_valid("()")
    assert solution._is_valid("()[]{}")
    assert solution._is_valid("{[()]}")

def test_invalid_cases(solution):
    assert not solution._is_valid("(]")
    assert not solution._is_valid("([)]")
    assert not solution._is_valid("(")
    assert not solution._is_valid("]")

def test_empty_string(solution):
    assert solution._is_valid("")
