from collections import deque


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Entry point for LeetCode submission.  
    Implements tree serialization and deserialization using BFS traversal.

    Delegates to _serialize_bfs() and _deserialize_bfs() for actual logic.
    """

    def serialize(self, root: TreeNode) -> str:
        """
        Converts a binary tree into a comma-separated string representation.

        Args:
            root (TreeNode): Root node of the binary tree.

        Returns:
            str: Serialized string representing the tree.

        Time Complexity: O(n) — visit each node once.  
        Space Complexity: O(n) — store all node values.
        """
        return self._serialize_bfs(root)

    def deserialize(self, data: str) -> TreeNode:
        """
        Reconstructs the binary tree from its serialized string representation.

        Args:
            data (str): Serialized string representing the tree.

        Returns:
            TreeNode: Root of the reconstructed binary tree.

        Time Complexity: O(n)  
        Space Complexity: O(n)
        """
        return self._deserialize_bfs(data)

    def _serialize_bfs(self, root: TreeNode) -> str:
        """
        Internal BFS implementation for tree serialization.
        """
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # Remove trailing nulls for compactness
        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)

    def _deserialize_bfs(self, data: str) -> TreeNode:
        """
        Internal BFS implementation for tree deserialization.
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            # Left child
            if values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            # Right child
            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root
