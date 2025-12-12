from typing import List


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _tiling_rectangle() for actual implementation.
        """
        return self._tiling_rectangle(n, m)

    def _tiling_rectangle(self, n: int, m: int) -> int:
        """
        Internal implementation.  
        Using DFS for solving the Tiling a Rectangle problem.

        Approach:
            - Use DFS + Backtracking with strong pruning.
            - Represent the state using a height profile (list of column heights).
            - Always expand from the lowest column to minimize branching.
            - Try placing the largest possible square first to reduce search depth.
            - Prune paths when the current number of squares already exceeds the best result.

        Time Complexity: O(2^[n*m]) with heavy pruning.  
        Space Complexity: O(m) for the height profile + recursion stack.

        Args:
            n (int): Rectangle height.
            m (int): Rectangle width.

        Returns:
            int: Minimum number of squares required to tile the rectangle.
        """
        if n < m:
            n, m = m, n

        heights = [0] * m
        best = [float('inf')]

        def dfs(count: int):
            # Pruning: current solution already worse than best
            if count >= best[0]:
                return

            # If fully filled
            if all(h == n for h in heights):
                best[0] = count
                return

            # Choose the lowest column to expand from
            min_h = min(heights)
            idx = heights.index(min_h)

            # Maximum square we can place at this column
            max_size = min(n - min_h, m - idx)

            # Try squares from largest to smallest
            for size in range(max_size, 0, -1):
                if any(heights[i] != min_h for i in range(idx, idx + size)):
                    continue

                # Place square
                for i in range(idx, idx + size):
                    heights[i] += size

                dfs(count + 1)

                # Backtrack
                for i in range(idx, idx + size):
                    heights[i] -= size

        dfs(0)
        return best[0]
