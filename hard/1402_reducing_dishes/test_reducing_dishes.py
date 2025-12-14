import pytest
from reducing_dishes import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._max_satisfaction([-1, -8, 0, 5, -9]) == 14

def test_case_2(solution):
    assert solution._max_satisfaction([4, 3, 2]) == 20

def test_case_3(solution):
    assert solution._max_satisfaction([-1, -4, -5]) == 0

def test_case_4(solution):
    # Mixed positives and negatives
    assert solution._max_satisfaction([5, -2, -1, 0, 3]) == 33

def test_case_5(solution):
    # Large case to ensure performance
    arr = list(range(-50, 51))
    assert solution._max_satisfaction(arr) == 85850
