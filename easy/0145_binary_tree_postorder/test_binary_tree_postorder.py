import unittest
from binary_tree_postorder import Solution, TreeNode


# 🧪 Unit tests for internal logic `_postorder()`
class TestBinaryTreePostorder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _build_tree(self, values):
        """
        Builds a binary tree from a list of values using level-order.  
        None indicates missing node.
        """
        if not values:
            return None

        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()

        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()

        return root

    def test_example_1(self):
        root = self._build_tree([1, None, 2, 3])
        expected = [3, 2, 1]
        self.assertEqual(self.solution._postorder(root), expected)

    def test_single_node(self):
        root = self._build_tree([1])
        self.assertEqual(self.solution._postorder(root), [1])

    def test_empty_tree(self):
        self.assertEqual(self.solution._postorder(None), [])

    def test_complete_tree(self):
        root = self._build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution._postorder(root), [4, 5, 2, 6, 7, 3, 1])

    def test_left_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution._postorder(root), [3, 2, 1])

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution._postorder(root), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
