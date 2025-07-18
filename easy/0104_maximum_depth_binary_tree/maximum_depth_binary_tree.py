from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_max_depth()` for actual implementation.
        """
        return self._max_depth(root)

    def _max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Internal implementation.
        Recursively calculates the maximum depth (or height) of a binary tree, defined as the number of nodes
        along the longest path from the root node down to the farthest leaf node.

        At each node, it computes the depth of its left and right subtrees, then returns the greater of the two,
        plus one for the current node.

        Time Complexity: O(n) — where n is the number of nodes in the tree.
        Space Complexity: O(h) — where h is the height of the tree, due to the recursion stack.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the tree.
        """
        if root is None:
            return 0

        left_depth = self._max_depth(root.left)
        right_depth = self._max_depth(root.right)
        return 1 + max(left_depth, right_depth)
