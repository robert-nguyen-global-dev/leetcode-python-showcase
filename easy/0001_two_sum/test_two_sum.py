import pytest
from two_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_case_2(solution):
    assert solution._two_sum([3, 2, 4], 6) == [1, 2]

def test_case_3(solution):
    assert solution._two_sum([3, 3], 6) == [0, 1]
