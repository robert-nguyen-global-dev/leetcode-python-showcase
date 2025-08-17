import pytest
from hamming_distance import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution._hamming_distance(1, 4) == 2  # 1 (001) vs 4 (100)

def test_example2(solution):
    assert solution._hamming_distance(3, 1) == 1  # 3 (011) vs 1 (001)

def test_same_number(solution):
    assert solution._hamming_distance(7, 7) == 0

def test_large_numbers(solution):
    assert solution._hamming_distance(255, 0) == 8

def test_edge_case(solution):
    assert solution._hamming_distance(0, 0) == 0