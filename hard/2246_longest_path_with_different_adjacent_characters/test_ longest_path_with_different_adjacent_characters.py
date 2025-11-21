import pytest
from longest_path_with_different_adjacent_characters import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    assert solution._longest_path(parent, s) == 3

def test_case_2(solution):
    parent = [-1, 0, 0, 0]
    s = "aabc"
    assert solution._longest_path(parent, s) == 3

def test_case_3(solution):
    parent = [-1]
    s = "z"
    assert solution._longest_path(parent, s) == 1
