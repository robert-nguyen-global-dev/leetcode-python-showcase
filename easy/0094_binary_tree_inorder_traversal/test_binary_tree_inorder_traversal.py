import pytest
from typing import Optional, List
from collections import deque
from binary_tree_inorder_traversal import Solution, TreeNode


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
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
    ([1, None, 2, 3], [1, 3, 2]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
])
def test_inorder_traversal(tree_list, expected):
    solution = Solution()
    root = build_tree_from_list(tree_list)
    assert solution._inorder_traversal(root) == expected
