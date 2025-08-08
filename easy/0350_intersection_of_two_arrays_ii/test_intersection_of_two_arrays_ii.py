import pytest
from intersection_of_two_arrays_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_intersection(solution):
    assert solution._intersect([1, 2, 2, 1], [2, 2]) == [2, 2]

def test_no_common_elements(solution):
    assert solution._intersect([1, 2, 3], [4, 5, 6]) == []

def test_with_duplicates(solution):
    assert sorted(solution._intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]

def test_one_array_empty(solution):
    assert solution._intersect([], [1, 2, 3]) == []

def test_both_arrays_empty(solution):
    assert solution._intersect([], []) == []

def test_all_elements_common(solution):
    assert solution._intersect([1, 1, 1], [1, 1]) == [1, 1]

def test_unbalanced_sizes(solution):
    assert sorted(solution._intersect([1], [1, 1, 1, 1])) == [1]
