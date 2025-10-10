from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _build_tree() for actual implementation.
        """
        return self._build_tree(preorder, inorder)

    def _build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Internal implementation.  
        Using recursive to rebuild binary tree from preorder and inorder traversals.

        Time Complexity: O(n) — each node is created once, lookups are O(1).  
        Space Complexity: O(n) — recursion stack + hashmap.

        Args:
            preorder (List[int]): Preorder traversal (Root → Left → Right)
            inorder (List[int]): Inorder traversal (Left → Root → Right)

        Returns:
            TreeNode: Root of the reconstructed binary tree.
        """
        if not preorder or not inorder:
            return None

        # Build hash map for quick index lookup in inorder
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0  # pointer in preorder array

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct subtree
            if left > right:
                return None

            # Select the current root and increment preorder index
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # Build the root node
            root = TreeNode(root_val)

            # Build left and right subtrees using inorder boundaries
            inorder_index = idx_map[root_val]
            root.left = helper(left, inorder_index - 1)
            root.right = helper(inorder_index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
