import pytest
from excel_column_number import Solution


@pytest.fixture
def solution():
    return Solution()


def test_single_letter(solution):
    assert solution._title_to_number("A") == 1
    assert solution._title_to_number("Z") == 26

def test_double_letter(solution):
    assert solution._title_to_number("AA") == 27
    assert solution._title_to_number("AZ") == 52
    assert solution._title_to_number("ZZ") == 702

def test_triple_letter(solution):
    assert solution._title_to_number("AAA") == 703
    assert solution._title_to_number("ABC") == 731

def test_large_column(solution):
    assert solution._title_to_number("FXSHRXW") == 2147483647  # Max 32-bit int
