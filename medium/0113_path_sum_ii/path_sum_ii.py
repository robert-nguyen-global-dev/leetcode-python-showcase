# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _path_sum_dfs() for actual implementation.
        """
        return self._path_sum_dfs(root, targetSum)

    def _path_sum_dfs(self, root: TreeNode, targetSum: int):
        """
        Internal implementation.  
        Uses DFS + Backtracking to find all root-to-leaf paths
        where the sum of node values equals targetSum.

        Time Complexity: O(n) — visit each node once.  
        Space Complexity: O(h) — recursion depth (height of tree).

        Args:
            root (TreeNode): Root node of the binary tree.
            targetSum (int): Target sum to achieve.

        Returns:
            List[List[int]]: All valid root-to-leaf paths whose sum equals targetSum.
        """
        res = []

        def dfs(node, total, path):
            if not node:
                return

            # Add current node to path and update total
            path.append(node.val)
            total += node.val

            # Check if leaf and sum matches
            if not node.left and not node.right and total == targetSum:
                res.append(path[:])

            # Recurse left and right
            dfs(node.left, total, path)
            dfs(node.right, total, path)

            # Backtrack
            path.pop()

        dfs(root, 0, [])
        return res
