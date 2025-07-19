import unittest
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


# 🧪 Unit tests for internal logic `_max_depth`
class TestMaximumDepthBinaryTree(unittest.TestCase):
    def test_case_1(self):
        root = build_tree_from_list([3, 9, 20, None, None, 15, 7])
        self.assertEqual(Solution()._max_depth(root), 3)

    def test_case_2(self):
        root = build_tree_from_list([1, None, 2])
        self.assertEqual(Solution()._max_depth(root), 2)

    def test_case_empty(self):
        root = build_tree_from_list([])
        self.assertEqual(Solution()._max_depth(root), 0)

    def test_case_single_node(self):
        root = build_tree_from_list([42])
        self.assertEqual(Solution()._max_depth(root), 1)


if __name__ == '__main__':
    unittest.main()
