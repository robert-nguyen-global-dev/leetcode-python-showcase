import pytest
from permutations import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [1, 2, 3]
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert sorted(solution._permute(nums)) == sorted(expected)

def test_two_elements(solution):
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    assert sorted(solution._permute(nums)) == sorted(expected)

def test_single_element(solution):
    nums = [5]
    expected = [[5]]
    assert solution._permute(nums) == expected

def test_empty_list(solution):
    nums = []
    expected = [[]]
    assert solution._permute(nums) == expected
