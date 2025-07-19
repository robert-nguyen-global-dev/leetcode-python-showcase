from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_symmetric()` for actual implementation.
        """
        return self._is_symmetric(root)

    def _is_symmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Internal implementation.  
        Determines whether a binary tree is symmetric around its center, meaning the left and right subtrees
        are mirror images of each other.

        The algorithm performs a recursive check by comparing mirrored node pairs from the left and right subtrees,
        ensuring structural and value symmetry at each level.

        Time Complexity: O(n) — where n is the number of nodes in the tree.  
        Space Complexity: O(h) — where h is the height of the tree, due to the recursion stack.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the binary tree is symmetric, False otherwise.
        """
        def is_mirror(left_subtree: Optional[TreeNode], right_subtree: Optional[TreeNode]) -> bool:
            if left_subtree is None and right_subtree is None:
                return True
            if left_subtree is None or right_subtree is None:
                return False
            return (
                left_subtree.val == right_subtree.val
                and is_mirror(left_subtree.left, right_subtree.right)
                and is_mirror(left_subtree.right, right_subtree.left)
            )

        return is_mirror(root, root)
