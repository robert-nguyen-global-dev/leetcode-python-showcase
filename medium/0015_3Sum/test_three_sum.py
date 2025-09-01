import pytest
from three_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(solution._three_sum(nums)) == sorted(expected)

def test_no_triplets(solution):
    nums = [1, 2, 3]
    assert solution._three_sum(nums) == []

def test_all_zeros(solution):
    nums = [0, 0, 0, 0]
    assert solution._three_sum(nums) == [[0, 0, 0]]

def test_large_negative_and_positive(solution):
    nums = [-5, 2, 3, 0, 1, -2]
    # expected = [[-5, 2, 3], [-2, 1, 1]] if [1,1] existed but in this case:
    expected = [[-5, 2, 3], [-2, 0, 2]]
    assert sorted(solution._three_sum(nums)) == sorted(expected)

def test_duplicates_handling(solution):
    nums = [-2, 0, 0, 2, 2]
    expected = [[-2, 0, 2]]
    assert solution._three_sum(nums) == expected

def test_empty_array(solution):
    assert solution._three_sum([]) == []

def test_single_element(solution):
    assert solution._three_sum([0]) == []
