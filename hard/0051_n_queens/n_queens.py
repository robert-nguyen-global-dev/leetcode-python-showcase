class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _solve_n_queens() for actual implementation.
        """
        return self._solve_n_queens(n)

    def _solve_n_queens(self, n: int) -> list[list[str]]:
        """
        Internal implementation.  
        Using backtracking.

        Idea:
        - Place one Queen per row.
        - Track columns and diagonals under attack using sets.
        - Recursively explore all valid placements.
        - When reaching row == n, build the board configuration.

        Time Complexity: O(N!)  
        Space Complexity: O(N) — recursion depth + sets.

        Args:
            n (int): Size of the chessboard (N x N).

        Returns:
            List[List[str]]: All valid board configurations.
        """
        def backtrack(row: int):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ['.'] * n
                    row_str[positions[i]] = 'Q'
                    board.append(''.join(row_str))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # choose
                positions[row] = col
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # explore
                backtrack(row + 1)

                # unchoose
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []
        cols, diag1, diag2 = set(), set(), set()
        positions = [-1] * n
        backtrack(0)
        return result
