# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _clone_graph() for actual implementation.
        """
        return self._clone_graph(node)

    def _clone_graph(self, node: 'Node') -> 'Node':
        """
        Internal implementation.  
        Uses hash map to record cloned nodes and recursively copy neighbors.

        Time Complexity: O(V + E) — visit every node and edge once.  
        Space Complexity: O(V) — hash map + recursion stack.

        Args:
            node (Node): Starting node of the original graph.

        Returns:
            Node: Deep-copied graph starting from cloned node.
        """
        if not node:
            return None

        old_to_new = {}

        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]

            # Clone node
            copy = Node(n.val)
            old_to_new[n] = copy

            # Clone all neighbors recursively
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
