import unittest
from path_sum import Solution, TreeNode
from typing import Optional


def build_tree_from_list(values: list) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order list with None values.
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    for idx, node in enumerate(nodes):
        node = nodes[idx]
        if node is not None:
            left_index = 2 * idx + 1
            right_index = 2 * idx + 2
            if left_index < len(nodes):
                node.left = nodes[left_index]
            if right_index < len(nodes):
                node.right = nodes[right_index]
                
    return nodes[0]


class TestPathSum(unittest.TestCase):
    def test_example_1(self):
        root = build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        self.assertTrue(Solution()._has_path_sum(root, 22))

    def test_example_2(self):
        root = build_tree_from_list([1, 2, 3])
        self.assertFalse(Solution()._has_path_sum(root, 5))

    def test_null_tree(self):
        self.assertFalse(Solution()._has_path_sum(None, 0))

    def test_single_node_true(self):
        root = build_tree_from_list([1])
        self.assertTrue(Solution()._has_path_sum(root, 1))

    def test_single_node_false(self):
        root = build_tree_from_list([1])
        self.assertFalse(Solution()._has_path_sum(root, 2))


if __name__ == '__main__':
    unittest.main()
