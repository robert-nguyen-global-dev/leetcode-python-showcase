from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_inorder_traversal()` for actual implementation.
        """
        return self._inorder_traversal(root)

    def _inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Internal implementation.
        Performs inorder traversal of a binary tree (Left → Node → Right).

        Time: O(n) where n is the number of nodes in the tree.
        Space: O(n) for the result list and recursion stack in the worst case.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: List of node values in inorder.
        """
        result: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
