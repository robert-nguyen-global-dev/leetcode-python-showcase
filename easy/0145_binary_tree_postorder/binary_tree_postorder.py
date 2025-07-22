from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Entry point for LeetCode submission.          
        Wrapper method to comply with LeetCode's required method signature.

        Delegates to `_postorder()` for internal method.
        """
        return self._postorder(root)

    def _postorder(self, root: Optional[TreeNode]) -> List[int]:
        """
        Internal implementation.  
        Performs postorder traversal of a binary tree using an iterative approach with a stack.

        The method simulates postorder traversal (left → right → root) by reversing
        a modified preorder traversal (root → right → left). It avoids recursion, making
        it safe for large/deep trees and suitable for production use in constrained environments.

        Time Complexity: O(n) — visits each node exactly once, where n is number of nodes.  
        Space Complexity: O(n) — worst case stack holds all nodes.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            List[int]: A list of node values in postorder traversal.
        """
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]
