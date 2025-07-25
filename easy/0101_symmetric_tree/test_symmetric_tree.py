import pytest
from typing import List, Optional
from collections import deque
from symmetric_tree import Solution, TreeNode


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


@pytest.mark.parametrize("tree_list, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),             # symmetric
    ([1, 2, 2, None, 3, None, 3], False),      # asymmetric
    ([], True),                                # empty tree
    ([1], True),                               # single node
])
def test_is_symmetric(tree_list, expected):
    solution = Solution()
    root = build_tree_from_list(tree_list)
    assert solution._is_symmetric(root) == expected
