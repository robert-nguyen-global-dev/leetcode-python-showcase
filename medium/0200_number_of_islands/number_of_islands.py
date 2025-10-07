from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _num_islands() for actual implementation.
        """
        return self._num_islands(grid)

    def _num_islands(self, grid: List[List[str]]) -> int:
        """
        Internal implementation.  
        Using DFS flood fill. Counts connected components of '1's (land) in a 2D grid.

        Time Complexity: O(m * n) — visit each cell once.  
        Space Complexity: O(m * n) — recursion stack in the worst case.

        Args:
            grid (List[List[str]]): 2D grid map of '1's (land) and '0's (water).

        Returns:
            int: Number of distinct islands.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            """
            Recursive DFS helper to mark connected land as visited ('0').
            """
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
