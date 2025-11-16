class Solution:
    def cherryPickup(self, grid):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _cherry_pickup() for actual implementation.
        """
        return self._cherry_pickup(grid)

    def _cherry_pickup(self, grid):
        """
        Internal implementation.  
        Dynamic Programming with bottom-up tabulation.

        Time Complexity: O(R * C^2 * 9). 
        Space Complexity: O(C^2)

        Args:
            grid (List[List[int]]): 2D grid of cherries.

        Returns:
            int: Maximum cherries two robots can collect.
        """
        rows, cols = len(grid), len(grid[0])

        # dp[c1][c2] represents the current row DP state
        dp = [[0] * cols for _ in range(cols)]

        # Initialize for the last row
        for c1 in range(cols):
            for c2 in range(cols):
                if c1 == c2:
                    dp[c1][c2] = grid[rows - 1][c1]
                else:
                    dp[c1][c2] = grid[rows - 1][c1] + grid[rows - 1][c2]

        # Bottom-up DP
        for r in range(rows - 2, -1, -1):
            new_dp = [[0] * cols for _ in range(cols)]
            for c1 in range(cols):
                for c2 in range(cols):
                    best = 0
                    for d1 in (-1, 0, 1):
                        for d2 in (-1, 0, 1):
                            nc1, nc2 = c1 + d1, c2 + d2
                            if 0 <= nc1 < cols and 0 <= nc2 < cols:
                                best = max(best, dp[nc1][nc2])

                    cherries = grid[r][c1]
                    if c1 != c2:
                        cherries += grid[r][c2]

                    new_dp[c1][c2] = best + cherries

            dp = new_dp

        return dp[0][cols - 1]
