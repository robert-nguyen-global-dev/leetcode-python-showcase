from typing import Optional


class TreeNode:
    """
    Standard LeetCode binary tree node.
    """
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_path_sum() for actual implementation.
        """
        return self._max_path_sum(root)

    def _max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Internal implementation.  
        Using DFS.

        For each node:
        - Compute left/right maximum gain.
        - Ignore negative gains.
        - Update global best using: val + left_gain + right_gain.
        - Return to parent only one side: val + max(left_gain, right_gain).

        Time Complexity: O(n)  
        Space Complexity: O(h) recursion stack (h = height of tree)

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            int: Maximum path sum of any path in the tree.
        """
        self.global_max = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # compute gain from left & right (negative values dropped)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # best path passing through this node
            best_through_node = node.val + left_gain + right_gain
            self.global_max = max(self.global_max, best_through_node)

            # return the best single-branch gain upward
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.global_max
