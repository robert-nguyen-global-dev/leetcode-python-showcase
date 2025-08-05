import pytest
from move_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_list, expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 1], [1, 0, 0]),
    ([4, 0, 5, 0, 0, 6], [4, 5, 6, 0, 0, 0]),
])
def test_move_zeroes(solution, input_list, expected):
    solution._move_zeroes(input_list)
    assert input_list == expected
