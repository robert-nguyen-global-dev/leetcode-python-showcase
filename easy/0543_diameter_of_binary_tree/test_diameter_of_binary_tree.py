import pytest
from diameter_of_binary_tree import Solution, TreeNode


@pytest.fixture
def solution():
    return Solution()


def build_tree(values):
    """Helper to build a binary tree from a list using BFS."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def test_example1(solution):
    # Input: [1,2,3,4,5]
    root = build_tree([1, 2, 3, 4, 5])
    assert solution._diameter_of_binary_tree(root) == 3

def test_single_node(solution):
    root = TreeNode(1)
    assert solution._diameter_of_binary_tree(root) == 0

def test_two_nodes(solution):
    root = build_tree([1, 2])
    assert solution._diameter_of_binary_tree(root) == 1

def test_unbalanced_tree(solution):
    # Input: [1,2,None,3,None,4,None]
    root = build_tree([1, 2, None, 3, None, 4, None])
    assert solution._diameter_of_binary_tree(root) == 3

def test_empty_tree(solution):
    assert solution._diameter_of_binary_tree(None) == 0
