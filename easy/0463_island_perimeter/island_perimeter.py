from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_island_perimeter()` for actual implementation.
        """
        return self._island_perimeter(grid)

    def _island_perimeter(self, grid: List[List[int]]) -> int:
        """
        Internal implementation.  
        Computes the perimeter of the island represented in the grid.

        Approach:
        - Traverse each cell in the grid.
        - For each land cell (1), start with 4 edges.
        - Subtract 1 edge for each neighboring land cell (up and left only to avoid double-counting).
        - Accumulate the total perimeter.

        Time Complexity: O(m * n) — where m, n are grid dimensions.  
        Space Complexity: O(1) — constant extra space.

        Args:
            grid (List[List[int]]): 2D grid with 0 = water, 1 = land.

        Returns:
            int: Total perimeter of the island.
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Start with 4 edges
                    perimeter += 4

                    # Check up
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2

                    # Check left
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2

        return perimeter
