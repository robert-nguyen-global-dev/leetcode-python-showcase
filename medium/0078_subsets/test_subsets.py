import pytest
from subsets import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 2, 3]
    result = solution._subsets(nums)
    expected = [
        [], [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ]
    assert sorted(result) == sorted(expected)

def test_case_2(solution):
    nums = [0]
    assert solution._subsets(nums) == [[], [0]]

def test_case_3(solution):
    nums = []
    assert solution._subsets(nums) == [[]]
