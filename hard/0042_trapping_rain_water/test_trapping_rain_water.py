import pytest
from trapping_rain_water import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert solution._trap(height) == 6

def test_case_2(solution):
    height = [4,2,0,3,2,5]
    assert solution._trap(height) == 9

def test_case_empty(solution):
    height = []
    assert solution._trap(height) == 0
