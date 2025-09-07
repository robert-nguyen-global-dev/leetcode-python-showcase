import pytest
from jump_game_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [2, 3, 1, 1, 4]
    assert solution._jump_game_ii(nums) == 2

def test_example_case_2(solution):
    nums = [2, 3, 0, 1, 4]
    assert solution._jump_game_ii(nums) == 2

def test_single_element(solution):
    nums = [0]
    assert solution._jump_game_ii(nums) == 0

def test_two_elements(solution):
    nums = [1, 2]
    assert solution._jump_game_ii(nums) == 1

def test_large_case(solution):
    nums = [1] * 1000
    assert solution._jump_game_ii(nums) == 999

def test_already_at_end(solution):
    nums = [5, 1, 1, 1, 1]
    assert solution._jump_game_ii(nums) == 1
