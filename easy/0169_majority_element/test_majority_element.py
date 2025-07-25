import pytest
from majority_element import Solution


@pytest.fixture
def solution():
    return Solution()


def test_majority_middle(solution):
    assert solution._majority_element([3, 2, 3]) == 3

def test_majority_single(solution):
    assert solution._majority_element([1]) == 1

def test_majority_end(solution):
    assert solution._majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

def test_majority_even_length(solution):
    assert solution._majority_element([1, 1, 2, 1]) == 1

def test_large_majority(solution):
    assert solution._majority_element([5]*100 + [1]*49) == 5
