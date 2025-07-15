import unittest
from symmetric_tree import Solution, TreeNode


def build_tree_from_list(values: list) -> TreeNode:
    """
    Helper to build binary tree from level-order list.
    None indicates missing nodes.
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    i = 0
    for idx, node in enumerate(nodes):
        if node is not None:
            left_index = 2 * idx + 1
            right_index = 2 * idx + 2
            if left_index < len(nodes):
                node.left = nodes[left_index]
            if right_index < len(nodes):
                node.right = nodes[right_index]
    return nodes[0]


# 🧪 Unit tests for internal logic `_is_symmetric`
class TestSymmetricTree(unittest.TestCase):
    def test_symmetric_tree(self):
        root = build_tree_from_list([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(Solution()._is_symmetric(root))

    def test_asymmetric_tree(self):
        root = build_tree_from_list([1, 2, 2, None, 3, None, 3])
        self.assertFalse(Solution()._is_symmetric(root))

    def test_empty_tree(self):
        root = build_tree_from_list([])
        self.assertTrue(Solution()._is_symmetric(root))

    def test_single_node(self):
        root = build_tree_from_list([1])
        self.assertTrue(Solution()._is_symmetric(root))


if __name__ == '__main__':
    unittest.main()
