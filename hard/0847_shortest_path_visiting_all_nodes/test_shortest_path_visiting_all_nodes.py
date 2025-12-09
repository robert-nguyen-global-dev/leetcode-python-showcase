import pytest
from shortest_path_visiting_all_nodes import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    graph = [[1, 2, 3], [0], [0], [0]]
    assert solution._shortest_path_length(graph) == 4

def test_case_2(solution):
    graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    assert solution._shortest_path_length(graph) == 4

def test_case_3(solution):
    graph = [[1], [0]]
    assert solution._shortest_path_length(graph) == 1
