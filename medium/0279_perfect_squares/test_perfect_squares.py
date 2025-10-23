import pytest
from perfect_squares import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    n = 12
    assert solution._num_squares(n) == 3  # 4 + 4 + 4

def test_case_2(solution):
    n = 13
    assert solution._num_squares(n) == 2  # 9 + 4

def test_case_3(solution):
    n = 1
    assert solution._num_squares(n) == 1  # 1
