import pytest
from typing import List, Optional
from collections import deque
from maximum_depth_binary_tree import Solution, TreeNode


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

        # Left child
        if index < len(values):
            left_val = values[index]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            index += 1

        # Right child
        if index < len(values):
            right_val = values[index]
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            index += 1

    return root


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([42], 1),
    ]
)
def test_max_depth(tree_list, expected):
    root = build_tree_from_list(tree_list)
    assert Solution()._max_depth(root) == expected
