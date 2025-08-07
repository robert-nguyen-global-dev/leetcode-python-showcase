import pytest
from reverse_string import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("input_str, expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["a"], ["a"]),
    ([], []),
])
def test_reverse_string(solution, input_str, expected):
    solution._reverse_string(input_str)
    assert input_str == expected
