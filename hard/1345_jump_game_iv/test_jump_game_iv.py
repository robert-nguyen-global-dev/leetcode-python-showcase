import pytest
from jump_game_iv import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    assert solution._min_jumps(arr) == 3

def test_case_2(solution):
    arr = [7]
    assert solution._min_jumps(arr) == 0

def test_case_3(solution):
    arr = [7, 6, 9, 6, 9, 6, 9, 7]
    assert solution._min_jumps(arr) == 1
