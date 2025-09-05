import pytest
from combination_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    assert sorted(solution._combination_sum(candidates, target)) == sorted(expected)

def test_example_case_2(solution):
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted(solution._combination_sum(candidates, target)) == sorted(expected)

def test_single_candidate(solution):
    candidates = [3]
    target = 9
    expected = [[3, 3, 3]]
    assert solution._combination_sum(candidates, target) == expected

def test_no_solution(solution):
    candidates = [2]
    target = 1
    expected = []
    assert solution._combination_sum(candidates, target) == expected

def test_empty_candidates(solution):
    candidates = []
    target = 7
    expected = []
    assert solution._combination_sum(candidates, target) == expected
