import pytest
from combination_sum_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    candidates = [10,1,2,7,6,1,5]
    target = 8
    expected = [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]
    assert sorted(solution._combination_sum_ii(candidates, target)) == sorted(expected)

def test_example_case_2(solution):
    candidates = [2,5,2,1,2]
    target = 5
    expected = [
        [1,2,2],
        [5]
    ]
    assert sorted(solution._combination_sum_ii(candidates, target)) == sorted(expected)

def test_no_solution(solution):
    candidates = [4,5,11]
    target = 3
    expected = []
    assert solution._combination_sum_ii(candidates, target) == expected

def test_single_candidate(solution):
    candidates = [3]
    target = 3
    expected = [[3]]
    assert solution._combination_sum_ii(candidates, target) == expected

def test_empty_candidates(solution):
    candidates = []
    target = 5
    expected = []
    assert solution._combination_sum_ii(candidates, target) == expected
