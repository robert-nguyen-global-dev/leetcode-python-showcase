import pytest
from max_value_of_equation import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    points = [[1, 3], [2, 0], [5, 10], [6, -10]]
    k = 1
    assert solution._find_max_value_of_equation(points, k) == 4

def test_case_2(solution):
    points = [[0, 0], [3, 0], [7, 0], [10, 0]]
    k = 5
    # (0 + 0) + (7 - 0) = 7
    assert solution._find_max_value_of_equation(points, k) == 4

def test_case_3(solution):
    points = [[1, 1], [3, 2], [6, 3], [10, 4]]
    k = 3
    # best is (3,2) with (6,3): (2+3)+(6-3) = 8
    assert solution._find_max_value_of_equation(points, k) == 8

def test_case_no_valid(solution):
    points = [[1, 5], [100, 10]]
    k = 10
    # No indexes satisfy |x_j - x_i| <= k
    assert solution._find_max_value_of_equation(points, k) == float('-inf')
