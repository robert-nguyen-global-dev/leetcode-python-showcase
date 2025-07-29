import pytest
from contains_duplicate import Solution


@pytest.fixture
def solution():
    return Solution()


def test_duplicates_present(solution):
    assert solution._contains_duplicate([1, 2, 3, 1]) is True

def test_no_duplicates(solution):
    assert solution._contains_duplicate([1, 2, 3, 4]) is False

def test_single_element(solution):
    assert solution._contains_duplicate([5]) is False

def test_large_input_with_duplicates(solution):
    assert solution._contains_duplicate(list(range(10**5)) + [0]) is True

def test_all_duplicates(solution):
    assert solution._contains_duplicate([7, 7, 7, 7]) is True
