import unittest
from binary_tree_inorder_traversal import Solution, TreeNode


def build_tree_from_list(values: list) -> TreeNode:
    """
    Helper to build binary tree from list using level-order traversal.
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


# 🧪 Unit tests for internal logic `_inorder_traversal`
class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def test_case_1(self):
        root = build_tree_from_list([1, None, 2, 3])
        expected = [1, 3, 2]
        self.assertEqual(Solution()._inorder_traversal(root), expected)

    def test_case_2(self):
        root = build_tree_from_list([])
        expected = []
        self.assertEqual(Solution()._inorder_traversal(root), expected)

    def test_case_3(self):
        root = build_tree_from_list([1])
        expected = [1]
        self.assertEqual(Solution()._inorder_traversal(root), expected)

    def test_case_4(self):
        root = build_tree_from_list([1, 2, 3, 4, 5])
        expected = [4, 2, 5, 1, 3]
        self.assertEqual(Solution()._inorder_traversal(root), expected)


if __name__ == '__main__':
    unittest.main()
