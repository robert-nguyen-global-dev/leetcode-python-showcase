import pytest
from binary_tree_level_order import Solution, TreeNode


@pytest.fixture
def sample_tree():
    # Tree structure:
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def test_case_1(sample_tree):
    sol = Solution()
    expected = [[3], [9, 20], [15, 7]]
    assert sol._level_order(sample_tree) == expected

def test_case_2():
    sol = Solution()
    assert sol._level_order(None) == []

def test_case_3():
    sol = Solution()
    root = TreeNode(1)
    assert sol._level_order(root) == [[1]]
