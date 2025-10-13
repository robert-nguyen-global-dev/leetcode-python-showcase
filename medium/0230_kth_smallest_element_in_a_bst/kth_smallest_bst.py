# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required signature.

        Delegates to _kth_smallest() for actual implementation.
        """
        return self._kth_smallest(root, k)

    def _kth_smallest(self, root: TreeNode, k: int) -> int:
        """
        Internal implementation.  
        Using iterative inorder traversal.

        Strategy:
            - Use stack to simulate recursion.
            - Traverse Left -> Node -> Right order.
            - Count nodes; when count == k, return current node value.

        Time Complexity: O(H + k) — where H = height of the tree.  
        Space Complexity: O(H) — due to stack.

        Args:
            root (TreeNode): Root of the BST.
            k (int): The k-th rank to find.

        Returns:
            int: The value of the k-th smallest node.
        """
        stack = []
        current = root
        count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1
            if count == k:
                return current.val

            current = current.right
