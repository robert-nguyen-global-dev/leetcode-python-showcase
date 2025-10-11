# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _flatten_tree() for actual implementation.
        """
        self._flatten_tree(root)

    def _flatten_tree(self, root: TreeNode) -> None:
        """
        Internal implementation.  
        Using recursive to flatten binary tree into a linked list in-place.

        Algorithm:
        - Traverse tree in reverse preorder (Right → Left → Root)
        - Maintain 'prev' pointer to connect nodes sequentially
        - For each node:
            node.right = prev
            node.left = None
            prev = node

        Time Complexity: O(n) — each node is visited once.  
        Space Complexity: O(h) — recursion stack (h = tree height).

        Args:
            root (TreeNode): Root of the binary tree.
        """
        self.prev = None

        def dfs(node):
            if not node:
                return
            # Step 1: Recurse right first
            dfs(node.right)
            # Step 2: Then recurse left
            dfs(node.left)
            # Step 3: Reconnect pointers
            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)
