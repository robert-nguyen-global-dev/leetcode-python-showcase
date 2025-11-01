import pytest
from n_queens import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_n_1(solution):
    expected = [["Q"]]
    assert solution._solve_n_queens(1) == expected

def test_case_n_4(solution):
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ]
    result = solution._solve_n_queens(4)
    assert sorted(result) == sorted(expected)
