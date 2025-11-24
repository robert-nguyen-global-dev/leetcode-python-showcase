import pytest
from jump_game_v import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
    d = 2
    assert solution._max_jumps(arr, d) == 4

def test_case_2(solution):
    arr = [3, 3, 3, 3, 3]
    d = 3
    assert solution._max_jumps(arr, d) == 1

def test_case_3(solution):
    arr = [7, 6, 5, 4, 3, 2, 1]
    d = 1
    assert solution._max_jumps(arr, d) == 7
