import pytest
from sum_of_left_leaves import Solution, TreeNode


@pytest.fixture
def tree1():
    # Tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    return root

@pytest.fixture
def tree2():
    # Tree:
    #   1
    root = TreeNode(1)
    return root

@pytest.fixture
def solution():
    return Solution()


def test_sum_of_left_leaves_example1(solution, tree1):
    assert solution._sum_of_left_leaves(tree1) == 24  # 9 + 15

def test_sum_of_left_leaves_example2(solution, tree2):
    assert solution._sum_of_left_leaves(tree2) == 0
