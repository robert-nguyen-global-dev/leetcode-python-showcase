import pytest
from n_queens_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_n_1(solution):
    assert solution._total_n_queens(1) == 1

def test_case_n_4(solution):
    assert solution._total_n_queens(4) == 2

def test_case_n_8(solution):
    # Classic 8-Queens problem: 92 distinct solutions
    assert solution._total_n_queens(8) == 92
