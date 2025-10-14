# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _rob_tree() for actual implementation.
        """
        return self._rob_tree(root)

    def _rob_tree(self, node: TreeNode) -> tuple[int, int]:
        """
        Internal implement.  
        Using recursive DP using postorder traversal.

        For each node, returns a tuple:
            (rob, not_rob)
            - rob: Max money if this node is robbed.
            - not_rob: Max money if this node is NOT robbed.

        Transition:
            rob = node.val + left.not_rob + right.not_rob
            not_rob = max(left.rob, left.not_rob) + max(right.rob, right.not_rob)

        Time Complexity: O(n) — each node visited once.  
        Space Complexity: O(h) — recursion depth.

        Args:
            node (TreeNode): Current node of the binary tree.

        Returns:
            tuple[int, int]: (rob, not_rob) values for current node.
        """
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)

        rob_val, not_rob_val = dfs(node)
        return max(rob_val, not_rob_val)
