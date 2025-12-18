from typing import List, Dict, Deque
from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _build_matrix() for the actual implementation.
        """
        return self._build_matrix(k, rowConditions, colConditions)

    def _build_matrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        Internal implementation.  
        Constructs a k x k matrix where integers 1..k appear exactly once,
        and obey the row and column precedence constraints.

        Approach:
            - Perform topological sort on rowConditions to determine row positions.
            - Perform topological sort on colConditions to determine column positions.
            - If either sort fails (cycle detected), return an empty matrix.
            - Otherwise, fill each value x at matrix[row_pos[x]][col_pos[x]].

        Time Complexity: O(k + E) for each topo-sort (E = number of conditions),
                         O(k^2) to build the final matrix.  
        Space Complexity: O(k + E).

        Args:
            k (int): Size of the matrix and the range of numbers.
            rowConditions (List[List[int]]): Constraints for row ordering.
            colConditions (List[List[int]]): Constraints for column ordering.

        Returns:
            List[List[int]]: A k x k matrix satisfying all constraints,
                             or an empty matrix if not possible.
        """
        row_order = self._topo_sort(k, rowConditions)
        col_order = self._topo_sort(k, colConditions)

        # If either is invalid → return empty matrix.
        if not row_order or not col_order:
            return []

        # Map value → row index and column index
        pos_row = {num: i for i, num in enumerate(row_order)}
        pos_col = {num: i for i, num in enumerate(col_order)}

        # Initialize empty matrix
        matrix = [[0] * k for _ in range(k)]

        # Place each number at its corresponding (row, column)
        for x in range(1, k + 1):
            matrix[pos_row[x]][pos_col[x]] = x

        return matrix

    def _topo_sort(self, k: int, conditions: List[List[int]]) -> List[int]:
        """
        Computes a topological ordering of nodes 1..k based on the given directed edges.

        Uses Kahn's Algorithm (BFS with indegree tracking).

        Returns:
            - A valid topological ordering as a list of length k.
            - Empty list if a cycle is detected (i.e., no valid ordering).
        """
        graph: Dict[int, List[int]] = {i: [] for i in range(1, k + 1)}
        indegree = {i: 0 for i in range(1, k + 1)}

        # Build graph and indegree
        for a, b in conditions:
            graph[a].append(b)
            indegree[b] += 1

        # BFS queue for nodes with indegree = 0
        q: Deque[int] = deque([node for node in range(1, k + 1) if indegree[node] == 0])

        order = []
        while q:
            node = q.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # If order does not contain all nodes → cycle exists
        return order if len(order) == k else []
