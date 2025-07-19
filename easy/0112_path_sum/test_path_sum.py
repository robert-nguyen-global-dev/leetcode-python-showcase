import unittest
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


class TestPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        self.assertTrue(self.solution._has_path_sum(root, 22))

    def test_example_2(self):
        root = build_tree_from_list([1, 2, 3])
        self.assertFalse(self.solution._has_path_sum(root, 5))

    def test_null_tree(self):
        self.assertFalse(self.solution._has_path_sum(None, 0))

    def test_single_node_true(self):
        root = build_tree_from_list([1])
        self.assertTrue(self.solution._has_path_sum(root, 1))

    def test_single_node_false(self):
        root = build_tree_from_list([1])
        self.assertFalse(self.solution._has_path_sum(root, 2))


if __name__ == '__main__':
    unittest.main()
