import pytest
from lowest_common_ancestor_bt import Solution, TreeNode


@pytest.fixture
def sample_tree():
    # Tree:
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def test_case_1(sample_tree):
    sol = Solution()
    p = find_node(sample_tree, 5)
    q = find_node(sample_tree, 1)
    assert sol._lowest_common_ancestor(sample_tree, p, q).val == 3

def test_case_2(sample_tree):
    sol = Solution()
    p = find_node(sample_tree, 5)
    q = find_node(sample_tree, 4)
    assert sol._lowest_common_ancestor(sample_tree, p, q).val == 5

def test_case_3(sample_tree):
    sol = Solution()
    p = find_node(sample_tree, 7)
    q = find_node(sample_tree, 8)
    assert sol._lowest_common_ancestor(sample_tree, p, q).val == 3
