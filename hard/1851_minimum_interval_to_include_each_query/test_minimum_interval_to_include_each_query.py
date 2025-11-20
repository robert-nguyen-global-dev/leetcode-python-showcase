import pytest
from minimum_interval_to_include_each_query import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    assert solution._min_interval(intervals, queries) == [3,3,1,4]

def test_case_2(solution):
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    assert solution._min_interval(intervals, queries) == [2,-1,4,6]

def test_case_3(solution):
    intervals = []
    queries = [1,2,3]
    assert solution._min_interval(intervals, queries) == [-1,-1,-1]

def test_case_4(solution):
    intervals = [[5,10]]
    queries = [1,5,10,11]
    assert solution._min_interval(intervals, queries) == [-1,6,6,-1]
