import pytest
from roman_to_int import Solution


@pytest.fixture
def solution():
    return Solution()
    

def test_case_1(solution):
    assert solution._roman_to_int("III") == 3

def test_case_2(solution):
    assert solution._roman_to_int("IV") == 4

def test_case_3(solution):
    assert solution._roman_to_int("IX") == 9

def test_case_4(solution):
    assert solution._roman_to_int("LVIII") == 58  # L=50, V=5, III=3

def test_case_5(solution):
    assert solution._roman_to_int("MCMXCIV") == 1994  # M=1000, CM=900, XC=90, IV=4
