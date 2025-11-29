from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _longest_increasing_path() for actual implementation.
        """
        return self._longest_increasing_path(matrix)

    def _longest_increasing_path(self, matrix: List[List[int]]) -> int:
        """
        Internal implementation.  
        Computes the length of the longest strictly increasing path in a 2D matrix.

        Uses DFS + memoization to ensure each cell is computed once.

        Time Complexity: O(m * n)  
        Space Complexity: O(m * n) for memo + recursion stack.

        Args:
            matrix (List[List[int]]): 2D matrix of integers.

        Returns:
            int: Length of the longest increasing path.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            """
            DFS from cell (r, c) and return longest increasing path starting here.
            """
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1  # At least the cell itself

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    candidate = 1 + dfs(nr, nc)
                    max_len = max(max_len, candidate)

            memo[r][c] = max_len
            return max_len

        longest = 0
        for i in range(rows):
            for j in range(cols):
                longest = max(longest, dfs(i, j))

        return longest
