from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _swim_in_water() for actual implementation.
        """
        return self._swim_in_water(grid)

    def _swim_in_water(self, grid: List[List[int]]) -> int:
        """
        Internal implementation.  
        Using Min-Heap / Dijkstra approach.

        Time Complexity: O(N^2 log N)  
        Space Complexity: O(N^2)

        Args:
            grid (List[List[int]]): NxN grid of elevations

        Returns:
            int: minimum time to reach bottom-right
        """
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == N-1 and y == N-1:
                return time

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    heapq.heappush(heap, (max(time, grid[nx][ny]), nx, ny))