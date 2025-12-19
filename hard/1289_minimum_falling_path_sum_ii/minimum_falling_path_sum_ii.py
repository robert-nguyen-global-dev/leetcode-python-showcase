from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method signature.

        Delegates to _min_falling_path_sum() for the actual implementation.
        """
        return self._min_falling_path_sum(grid)

    def _min_falling_path_sum(self, grid: List[List[int]]) -> int:
        """
        Internal implementation.  
        Computes the minimum falling path sum with the constraint that
        adjacent selections cannot be from the same column.

        Approach:
            - Dynamic Programming optimized with min1/min2 technique.
            - For each row, track the smallest and second smallest cumulative
              DP values from the previous row along with their column indices.
            - When transitioning to dp[r][c], use:
                - min1 if c != min1_col
                - min2 if c == min1_col
            - This guarantees valid transitions and achieves O(n^2) time.

        Time Complexity: O(n^2) — Each row processed in O(n).  
        Space Complexity: O(n) — Only storing previous row DP.

        Args:
            grid (List[List[int]]): n x n matrix of integers.

        Returns:
            int: Minimum valid falling path sum.
        """
        n = len(grid)

        # dp holds dp for the previous row
        dp = grid[0][:]

        for r in range(1, n):
            # Find min1 and min2 from dp
            min1 = min2 = float("inf")
            min1_col = min2_col = -1

            for c in range(n):
                val = dp[c]
                if val < min1:
                    min2, min2_col = min1, min1_col
                    min1, min1_col = val, c
                elif val < min2:
                    min2, min2_col = val, c

            new_dp = [0] * n

            for c in range(n):
                # If using same column as min1 → must use min2
                best_prev = min2 if c == min1_col else min1
                new_dp[c] = grid[r][c] + best_prev

            dp = new_dp

        return min(dp)
