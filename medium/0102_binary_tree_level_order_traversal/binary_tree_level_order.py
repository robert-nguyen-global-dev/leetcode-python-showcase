from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _level_order() for actual implementation.
        """
        return self._level_order(root)

    def _level_order(self, root: TreeNode) -> list[list[int]]:
        """
        Internal implementation.  
        Using BFS-based for level order traversal.

        Time Complexity: O(n) — each node is visited once.  
        Space Complexity: O(n) — queue stores nodes level by level.

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            List[List[int]]: Nested list representing level order traversal.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
