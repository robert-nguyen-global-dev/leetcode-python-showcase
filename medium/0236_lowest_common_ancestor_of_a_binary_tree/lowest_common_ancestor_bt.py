# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _lowest_common_ancestor() for actual implementation.
        """
        return self._lowest_common_ancestor(root, p, q)

    def _lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Internal implementation.  
        Using recursive to find the lowest common ancestor of two nodes.

        Algorithm:
        - If root is None → return None.
        - If root equals p or q → return root.
        - Recursively find LCA in left and right subtrees.
        - If both sides return non-null → current root is the LCA.
        - Otherwise → propagate the non-null result upward.

        Time Complexity: O(n) — each node visited once.  
        Space Complexity: O(h) — recursion stack (h = tree height).

        Args:
            root (TreeNode): Root of the binary tree.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            TreeNode: The lowest common ancestor node.
        """
        if not root or root == p or root == q:
            return root

        left = self._lowest_common_ancestor(root.left, p, q)
        right = self._lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        return left or right
