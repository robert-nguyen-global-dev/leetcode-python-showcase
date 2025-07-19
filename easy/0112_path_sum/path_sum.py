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
        Wrapper method to comply with LeetCode's required method name.
		
        Delegates to `_has_path_sum()` for actual implementation.
        """
        return self._has_path_sum(root, targetSum)

    def _has_path_sum(self, node: Optional[TreeNode], remaining_sum: int) -> bool:
        """
        Internal implementation.  
        Recursively determines if there exists a root-to-leaf path such that the sum of node values equals the target.

        At each node, it subtracts the current node's value from the remaining target sum and recursively checks
        left and right subtrees. If a leaf node is reached and the remaining sum is zero, a valid path is found.

        Time Complexity: O(n) — where n is the total number of nodes.  
        Space Complexity: O(h) — where h is the height of the tree due to the recursion stack.

        Args:
            node (Optional[TreeNode]): Current node being explored.
            remaining_sum (int): Remaining sum needed to reach the target path sum.

        Returns:
            bool: True if such a path exists from root to leaf, False otherwise.
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
