import pytest
from kth_smallest_bst import Solution, TreeNode


@pytest.fixture
def bst_sample():
    # Construct BST:
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    return root

@pytest.fixture
def solution():
    return Solution()


def test_case_1(bst_sample, solution):
    assert solution._kth_smallest(bst_sample, 3) == 3  # [1,2,3,4,5,6]

def test_case_2(bst_sample, solution):
    assert solution._kth_smallest(bst_sample, 1) == 1

def test_case_3(bst_sample, solution):
    assert solution._kth_smallest(bst_sample, 6) == 6
