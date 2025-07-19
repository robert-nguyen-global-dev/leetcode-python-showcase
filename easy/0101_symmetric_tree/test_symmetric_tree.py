import unittest
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


# 🧪 Unit tests for internal logic `_is_symmetric`
class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_symmetric_tree(self):
        root = build_tree_from_list([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.solution._is_symmetric(root))

    def test_asymmetric_tree(self):
        root = build_tree_from_list([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.solution._is_symmetric(root))

    def test_empty_tree(self):
        root = build_tree_from_list([])
        self.assertTrue(self.solution._is_symmetric(root))

    def test_single_node(self):
        root = build_tree_from_list([1])
        self.assertTrue(self.solution._is_symmetric(root))


if __name__ == '__main__':
    unittest.main()
