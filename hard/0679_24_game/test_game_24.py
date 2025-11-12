import pytest
from game_24 import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    cards = [4, 1, 8, 7]
    assert solution._judge_point_24(cards) is True  # (8 - 4) * (7 - 1) = 24


def test_case_2(solution):
    cards = [1, 2, 1, 2]
    assert solution._judge_point_24(cards) is False


def test_case_3(solution):
    cards = [3, 3, 8, 8]
    assert solution._judge_point_24(cards) is True  # (8 / (3 - 8/3)) = 24
