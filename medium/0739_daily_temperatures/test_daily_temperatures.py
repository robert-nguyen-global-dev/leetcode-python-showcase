import pytest
from daily_temperatures import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert solution._daily_temperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]

def test_case_2(solution):
    temperatures = [30, 40, 50, 60]
    assert solution._daily_temperatures(temperatures) == [1, 1, 1, 0]

def test_case_3(solution):
    temperatures = [30, 60, 90]
    assert solution._daily_temperatures(temperatures) == [1, 1, 0]
