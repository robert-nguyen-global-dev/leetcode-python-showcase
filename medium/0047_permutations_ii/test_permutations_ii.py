import pytest
from permutations_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1, 1, 2]
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert sorted(solution._permute_unique(nums)) == sorted(expected)

def test_case_2(solution):
    nums = [1, 2, 3]
    expected = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1]
    ]
    assert sorted(solution._permute_unique(nums)) == sorted(expected)

def test_case_3(solution):
    nums = [2, 2, 1, 1]
    result = solution._permute_unique(nums)
    assert len(result) == 6  # Có 6 hoán vị duy nhất
