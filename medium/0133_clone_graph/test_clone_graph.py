import pytest
from clone_graph import Solution, Node


@pytest.fixture
def build_graph():
    # Build a simple 4-node square graph: 1-2-3-4-1
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    return n1


def test_clone_graph_structure(build_graph):
    original = build_graph
    clone = Solution()._clone_graph(original)

    assert clone is not original
    assert clone.val == 1
    assert len(clone.neighbors) == 2
    assert all(c is not o for c, o in zip(clone.neighbors, original.neighbors))
    assert clone.neighbors[0].val in {2, 4}
    assert clone.neighbors[1].val in {2, 4}

def test_clone_graph_empty():
    assert Solution()._clone_graph(None) is None
