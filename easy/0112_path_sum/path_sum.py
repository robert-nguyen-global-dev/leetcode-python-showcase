from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Entry point for LeetCode submission.
        Delegates to `_has_path_sum()` for internal logic.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.
            targetSum (int): The desired sum along a root-to-leaf path.

        Returns:
            bool: True if such a path exists, False otherwise.
        """
        return self._has_path_sum(root, targetSum)

    def _has_path_sum(self, node: Optional[TreeNode], remaining_sum: int) -> bool:
        """
        Recursively checks whether a root-to-leaf path exists with the given sum.

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(h), where h is the height of the tree.

        Args:
            node (Optional[TreeNode]): Current node in traversal.
            remaining_sum (int): Remaining sum required for path.

        Returns:
            bool: True if such path exists, False otherwise.
        """
        if node is None:
            return False

        # Leaf node check
        if node.left is None and node.right is None:
            return remaining_sum == node.val

        # Recurse into subtrees
        left_has_path = self._has_path_sum(node.left, remaining_sum - node.val)
        right_has_path = self._has_path_sum(node.right, remaining_sum - node.val)

        return left_has_path or right_has_path
