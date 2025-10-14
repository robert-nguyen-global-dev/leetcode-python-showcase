import pytest
from house_robber_iii import Solution, TreeNode


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    # Tree: [3,2,3,None,3,None,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    assert solution._rob_tree(root) == 7


def test_case_2(solution):
    # Tree: [3,4,5,1,3,None,1]
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5, None, TreeNode(1))
    assert solution._rob_tree(root) == 9


def test_case_3(solution):
    assert solution._rob_tree(None) == 0
