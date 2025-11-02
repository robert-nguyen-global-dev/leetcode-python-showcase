class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _total_n_queens() for actual implementation.
        """
        return self._total_n_queens(n)

    def _total_n_queens(self, n: int) -> int:
        """
        Internal implementation.  
        Using backtracking.

        Idea:
        - Place one Queen per row.
        - Track columns and diagonals under attack using sets.
        - Recursively try placing Queens in safe columns per row.
        - Increment count when a valid board is found.

        Time Complexity: O(N!).  
        Space Complexity: O(N) — recursion depth + tracking sets.

        Args:
            n (int): Size of the chessboard (N x N).

        Returns:
            int: Number of distinct solutions.
        """
        def backtrack(row: int):
            nonlocal count
            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # choose
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # explore
                backtrack(row + 1)

                # unchoose
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        count = 0
        cols, diag1, diag2 = set(), set(), set()
        backtrack(0)
        return count
