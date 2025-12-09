from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _shortest_path_length() for actual implementation.
        """
        return self._shortest_path_length(graph)

    def _shortest_path_length(self, graph: List[List[int]]) -> int:
        """
        Internal implementation.  
        Using BFS over state space (node, mask).

        Time Complexity:  O(N * 2^N)  
        Space Complexity: O(N * 2^N)

        Args:
            graph (List[List[int]]): adjacency list

        Returns:
            int: minimum number of steps to visit all nodes
        """
        n = len(graph)
        if n == 1:
            return 0

        final_mask = (1 << n) - 1
        queue = deque()
        visited = [set() for _ in range(n)]

        # Multi-source BFS initialization
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask))
            visited[i].add(mask)

        steps = 0

        # BFS by layers
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()

                if mask == final_mask:
                    return steps

                # Explore neighbors
                for nei in graph[node]:
                    next_mask = mask | (1 << nei)
                    if next_mask not in visited[nei]:
                        visited[nei].add(next_mask)
                        queue.append((nei, next_mask))
            steps += 1

        return -1  # Should never happen for connected graphs
