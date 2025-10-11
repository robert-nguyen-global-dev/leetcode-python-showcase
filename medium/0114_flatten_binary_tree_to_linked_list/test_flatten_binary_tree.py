import pytest
from flatten_binary_tree import Solution, TreeNode


def tree_to_list(root):
    """Helper to convert flattened tree to list form (following right pointers)."""
    result = []
    while root:
        result.append(root.val)
        if root.left:
            raise AssertionError("Left child must be None after flattening")
        root = root.right
    return result

@pytest.fixture
def sample_tree():
    # Tree:
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(5, None, TreeNode(6))
    return root


def test_case_1(sample_tree):
    Solution()._flatten_tree(sample_tree)
    assert tree_to_list(sample_tree) == [1, 2, 3, 4, 5, 6]

def test_case_2():
    root = TreeNode(0)
    Solution()._flatten_tree(root)
    assert tree_to_list(root) == [0]

def test_case_3():
    Solution()._flatten_tree(None)  # Should not raise
