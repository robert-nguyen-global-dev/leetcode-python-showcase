import pytest
from basic_calculator_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    s = "3+2*2"
    assert solution._calculate(s) == 7

def test_case_2(solution):
    s = " 3/2 "
    assert solution._calculate(s) == 1

def test_case_3(solution):
    s = " 3+5 / 2 "
    assert solution._calculate(s) == 5

def test_case_4(solution):
    s = "14-3/2"
    # 14 - (3/2) = 14 - 1 = 13
    assert solution._calculate(s) == 13

def test_case_5(solution):
    s = "0-2147483647"
    assert solution._calculate(s) == -2147483647
