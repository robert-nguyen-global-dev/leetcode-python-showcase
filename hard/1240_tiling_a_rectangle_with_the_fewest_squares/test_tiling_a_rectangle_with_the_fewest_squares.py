import pytest
from tiling_a_rectangle_with_the_fewest_squares import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._tiling_rectangle(2, 3) == 3  # 2x3 requires 3 squares

def test_case_2(solution):
    assert solution._tiling_rectangle(5, 8) == 5

def test_case_3(solution):
    assert solution._tiling_rectangle(11, 13) == 6

def test_case_4(solution):
    assert solution._tiling_rectangle(1, 1) == 1

def test_case_5(solution):
    assert solution._tiling_rectangle(3, 3) == 1  # perfect square
