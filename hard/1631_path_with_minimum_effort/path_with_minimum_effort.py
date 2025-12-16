from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _minimum_effort_path() for actual implementation.
        """
        return self._minimum_effort_path(heights)

    def _minimum_effort_path(self, heights: List[List[int]]) -> int:
        """
        Internal implementation.  
        Computes the minimum effort path using Dijkstra's algorithm.

        Approach:
            - Treat each grid cell as a node.
            - Effort between adjacent cells = abs(height difference).
            - Path effort = max edge weight along the path.
            - Use a min-heap (priority queue) to always expand the cell
              with the currently smallest required effort.
            - Once reaching bottom-right, the effort is guaranteed minimal.

        Time Complexity: O(m * n * log[m * n])  
        Space Complexity: O(m * n)

        Args:
            heights (List[List[int]]): 2D grid of heights.

        Returns:
            int: Minimum possible effort to reach bottom-right.
        """
        m, n = len(heights), len(heights[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        effort = [[float('inf')] * n for _ in range(m)]

        min_heap = [(0, 0, 0)]  # (effort, r, c)
        effort[0][0] = 0

        while min_heap:
            cur_effort, r, c = heapq.heappop(min_heap)

            if r == m - 1 and c == n - 1:
                return cur_effort

            if cur_effort > effort[r][c]:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_effort = max(cur_effort, abs(heights[r][c] - heights[nr][nc]))
                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))

        return 0
