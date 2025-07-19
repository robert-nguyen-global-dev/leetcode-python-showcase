import unittest
from typing import List, Optional
from collections import deque
from binary_tree_inorder_traversal import Solution, TreeNode


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


# 🧪 Unit tests for internal logic `_inorder_traversal`
class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        root = build_tree_from_list([1, None, 2, 3])
        expected = [1, 3, 2]
        self.assertEqual(self.solution._inorder_traversal(root), expected)

    def test_case_2(self):
        root = build_tree_from_list([])
        expected = []
        self.assertEqual(self.solution._inorder_traversal(root), expected)

    def test_case_3(self):
        root = build_tree_from_list([1])
        expected = [1]
        self.assertEqual(self.solution._inorder_traversal(root), expected)

    def test_case_4(self):
        root = build_tree_from_list([1, 2, 3, 4, 5])
        expected = [4, 2, 5, 1, 3]
        self.assertEqual(self.solution._inorder_traversal(root), expected)


if __name__ == '__main__':
    unittest.main()
