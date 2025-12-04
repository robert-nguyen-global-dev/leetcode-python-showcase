import pytest
from erect_the_fence import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    result = solution._outer_trees(trees)
    expected = [[1,1],[2,0],[4,2],[3,3],[2,4]]
    for p in expected:
        assert p in result

def test_collinear_edge_points(solution):
    trees = [[0,0],[1,1],[2,2],[3,3]]
    result = solution._outer_trees(trees)
    # All should be included on boundary
    assert len(result) == 4

def test_square(solution):
    trees = [[0,0],[0,1],[1,1],[1,0]]
    result = solution._outer_trees(trees)
    assert len(result) == 4

def test_single_point(solution):
    assert solution._outer_trees([[5,5]]) == [[5,5]]

def test_two_points(solution):
    trees = [[1,2],[3,4]]
    assert len(solution._outer_trees(trees)) == 2
