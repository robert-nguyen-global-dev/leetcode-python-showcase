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
        Performs an inorder traversal of a binary tree (Left → Node → Right), collecting node values in sequence.

        This recursive approach visits all nodes while maintaining a call stack that mirrors the tree's structure.
        It ensures values are collected in the correct inorder sequence, useful in many binary search tree operations.

        Time Complexity: O(n) — where n is the number of nodes in the tree.
        Space Complexity: O(n) — for the recursion stack and result list in the worst case (completely unbalanced tree).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: List of node values collected in inorder.
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
