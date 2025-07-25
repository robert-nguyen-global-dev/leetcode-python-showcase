import pytest
from climbing_stairs import Solution


@pytest.fixture
def solution():
    return Solution()
    

def test_case_1(solution):
    assert solution._climb_stairs(1) == 1

def test_case_2(solution):
    assert solution._climb_stairs(2) == 2

def test_case_3(solution):
    assert solution._climb_stairs(3) == 3

def test_case_4(solution):
    assert solution._climb_stairs(4) == 5

def test_case_5(solution):
    assert solution._climb_stairs(10) == 89

def test_case_large(solution):
    assert solution._climb_stairs(45) == 1836311903
