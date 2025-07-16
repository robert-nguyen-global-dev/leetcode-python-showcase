import unittest
from maximum_depth_binary_tree import Solution, TreeNode


def build_tree_from_list(values: list) -> TreeNode:
    """
    Helper to build binary tree from level-order list.
    None indicates missing nodes.
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    for idx, node in enumerate(nodes):
        if node is not None:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
                
    return nodes[0]


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
