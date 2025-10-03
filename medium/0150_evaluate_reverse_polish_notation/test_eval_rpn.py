import pytest
from eval_rpn import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    tokens = ["2", "1", "+", "3", "*"]
    # ((2 + 1) * 3) = 9
    assert solution._evalRPN(tokens) == 9

def test_case_2(solution):
    tokens = ["4", "13", "5", "/", "+"]
    # (4 + (13 / 5)) = 6
    assert solution._evalRPN(tokens) == 6

def test_case_3(solution):
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # Evaluate step by step, expected result = 22
    assert solution._evalRPN(tokens) == 22

def test_single_number(solution):
    tokens = ["42"]
    assert solution._evalRPN(tokens) == 42

def test_negative_division(solution):
    tokens = ["-7", "3", "/"]
    # -7 / 3 = -2.333 → truncate toward 0 = -2
    assert solution._evalRPN(tokens) == -2
