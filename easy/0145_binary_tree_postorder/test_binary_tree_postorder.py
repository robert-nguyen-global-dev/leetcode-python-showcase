import pytest
from binary_tree_postorder import Solution, TreeNode


def build_tree(values):
    """
    Builds a binary tree from a list of values using level-order.  
    None indicates missing node.
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    root = build_tree([1, None, 2, 3])
    assert solution._postorder(root) == [3, 2, 1]

def test_single_node(solution):
    root = build_tree([1])
    assert solution._postorder(root) == [1]

def test_empty_tree(solution):
    assert solution._postorder(None) == []

def test_complete_tree(solution):
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution._postorder(root) == [4, 5, 2, 6, 7, 3, 1]

def test_left_skewed_tree(solution):
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert solution._postorder(root) == [3, 2, 1]

def test_right_skewed_tree(solution):
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert solution._postorder(root) == [3, 2, 1]
