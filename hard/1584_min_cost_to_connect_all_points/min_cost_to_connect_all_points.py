from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _min_cost_connect_points() for actual implementation.
        """
        return self._min_cost_connect_points(points)

    def _min_cost_connect_points(self, points: List[List[int]]) -> int:
        """
        Internal implementation.  
        Using Prim's algorithm.

        Time Complexity: O(n^2) — each point attempts to connect to all others.  
        Space Complexity: O(n) — visited array + distance array.

        Args:
            points (List[List[int]]): List of points [x, y].

        Returns:
            int: Minimum total cost to connect all points.
        """
        import heapq

        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0  # start from point 0

        heap = [(0, 0)]  # (cost, point index)
        total_cost = 0
        added = 0

        while added < n:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue

            visited[u] = True
            total_cost += cost
            added += 1

            x1, y1 = points[u]

            # Update neighbor distances
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost