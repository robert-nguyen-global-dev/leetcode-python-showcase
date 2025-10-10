import pytest
from construct_tree_pre_inorder import Solution, TreeNode


def tree_to_list(root):
    """Helper to convert tree into level-order list for easy comparison."""
    if not root:
        return []
    from collections import deque
    q, result = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution._build_tree(preorder, inorder)
    assert tree_to_list(root) == [3, 9, 20, None, None, 15, 7]

def test_case_2(solution):
    preorder = [-1]
    inorder = [-1]
    root = solution._build_tree(preorder, inorder)
    assert tree_to_list(root) == [-1]

def test_case_3(solution):
    preorder = [1, 2]
    inorder = [2, 1]
    root = solution._build_tree(preorder, inorder)
    assert tree_to_list(root) == [1, 2]
