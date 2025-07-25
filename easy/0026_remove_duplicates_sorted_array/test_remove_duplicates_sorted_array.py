import pytest
from remove_duplicates_sorted_array import Solution


@pytest.fixture
def solution():
    return Solution()


def test_sorted_array_with_duplicates(solution):
    nums = [1, 1, 2]
    expected = [1, 2]
    length = solution._remove_duplicates(nums)
    assert length == len(expected)
    assert nums[:length] == expected

def test_longer_sorted_array_with_duplicates(solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = [0, 1, 2, 3, 4]
    length = solution._remove_duplicates(nums)
    assert length == len(expected)
    assert nums[:length] == expected

def test_empty_array(solution):
    nums = []
    expected = []
    length = solution._remove_duplicates(nums)
    assert length == len(expected)
    assert nums[:length] == expected
