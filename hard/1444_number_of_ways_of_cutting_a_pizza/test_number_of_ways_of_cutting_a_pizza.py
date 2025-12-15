import pytest
from number_of_ways_of_cutting_a_pizza import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    pizza = ["A..", "AAA", "..."]
    assert solution._count_ways(pizza, 3) == 3

def test_case_2(solution):
    pizza = ["A", "A", "A"]
    assert solution._count_ways(pizza, 3) == 1

def test_case_3(solution):
    pizza = ["AA", "AA"]
    assert solution._count_ways(pizza, 2) == 2

def test_case_4(solution):
    pizza = ["A..", "..A", "..A"]
    assert solution._count_ways(pizza, 3) == 3

def test_case_5(solution):
    # Large rectangular case
    pizza = ["A.AA", ".A..", "..A.", "A..A"]
    assert solution._count_ways(pizza, 4) == 40
