import pytest
from typing import List, Optional
from collections import deque
from path_sum import Solution, TreeNode


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build binary tree from level-order list including None for missing nodes.
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values):
            left_val = values[index]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            index += 1

        if index < len(values):
            right_val = values[index]
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            index += 1

    return root


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    root = build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert solution._has_path_sum(root, 22) is True

def test_example_2(solution):
    root = build_tree_from_list([1, 2, 3])
    assert solution._has_path_sum(root, 5) is False

def test_null_tree(solution):
    assert solution._has_path_sum(None, 0) is False

def test_single_node_true(solution):
    root = build_tree_from_list([1])
    assert solution._has_path_sum(root, 1) is True

def test_single_node_false(solution):
    root = build_tree_from_list([1])
    assert solution._has_path_sum(root, 2) is False
