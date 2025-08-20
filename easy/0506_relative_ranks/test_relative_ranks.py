import pytest
from relative_ranks import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    score = [5, 4, 3, 2, 1]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert solution._find_relative_ranks(score) == expected

def test_example2(solution):
    score = [10, 3, 8, 9, 4]
    expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    assert solution._find_relative_ranks(score) == expected

def test_single_athlete(solution):
    score = [99]
    expected = ["Gold Medal"]
    assert solution._find_relative_ranks(score) == expected

def test_two_athletes(solution):
    score = [80, 90]
    expected = ["Silver Medal", "Gold Medal"]
    assert solution._find_relative_ranks(score) == expected

def test_tie_scores(solution):
    score = [100, 100, 90]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    assert solution._find_relative_ranks(score) == expected
