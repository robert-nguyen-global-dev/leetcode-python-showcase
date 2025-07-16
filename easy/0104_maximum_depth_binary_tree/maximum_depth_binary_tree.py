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
        Recursively computes the maximum depth of a binary tree.

        Time Complexity: O(n) — where n is the number of nodes.
        Space Complexity: O(h) — where h is the height of the tree (due to recursion stack).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: Maximum depth of the binary tree.
        """
        if root is None:
            return 0

        left_depth = self._max_depth(root.left)
        right_depth = self._max_depth(root.right)
        return 1 + max(left_depth, right_depth)
