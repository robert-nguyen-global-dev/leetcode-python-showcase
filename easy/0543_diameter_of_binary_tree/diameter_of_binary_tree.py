from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_diameter_of_binary_tree()` for actual implementation.
        """
        return self._diameter_of_binary_tree(root)

    def _diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        """
        Internal implementation.  
        Finds the diameter of a binary tree — the length of the longest path 
        between any two nodes in the tree.

        Approach:
        - Use DFS (post-order traversal) to compute subtree heights.
        - At each node:
            - Calculate left_height and right_height recursively.
            - Update the global diameter using left_height + right_height.
        - Return the height of the current subtree: 1 + max(left, right).

        Time Complexity: O(n) — visits each node once.  
        Space Complexity: O(h) — recursion stack where h is tree height (O(n) worst case).

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
        self.diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            # Update max diameter found so far
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter
