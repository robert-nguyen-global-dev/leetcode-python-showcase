import pytest
from binary_tree_maximum_path_sum import Solution, TreeNode


def build_tree(values):
    """
    Build binary tree from level-order list with None as empty nodes.
    """
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    child_idx = 1

    for idx, node in enumerate(nodes):
        if node is not None:
            if child_idx < len(nodes):
                node.left = nodes[child_idx]
                child_idx += 1
            if child_idx < len(nodes):
                node.right = nodes[child_idx]
                child_idx += 1

    return nodes[0]


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    root = build_tree([1, 2, 3])
    assert solution._max_path_sum(root) == 6

def test_case_2(solution):
    root = build_tree([-10, 9, 20, None, None, 15, 7])
    assert solution._max_path_sum(root) == 42

def test_case_3(solution):
    root = build_tree([2, -1])
    assert solution._max_path_sum(root) == 2

def test_case_4(solution):
    root = build_tree([-3])
    assert solution._max_path_sum(root) == -3
