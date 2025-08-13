from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_sum_of_left_leaves()` for actual implementation.
        """
        return self._sum_of_left_leaves(root)

    def _sum_of_left_leaves(self, root: Optional[TreeNode]) -> int:
        """
        Internal implementation.  
        Calculates the sum of all left leaf nodes in a binary tree.

        A leaf is a node with no left and right children.  
        A left leaf is a leaf that is the left child of its parent.

        Time Complexity: O(n) — where n is the number of nodes in the tree, 
        because each node is visited exactly once.  
        Space Complexity: O(h) — where h is the height of the tree, due to recursive call stack.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The sum of all left leaf values.
        """
        if not root:
            return 0

        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        total += self._sum_of_left_leaves(root.left)
        total += self._sum_of_left_leaves(root.right)
        
        return total
