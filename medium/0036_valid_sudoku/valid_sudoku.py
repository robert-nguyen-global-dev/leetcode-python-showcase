from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_valid_sudoku()` for actual implementation.
        """
        return self._is_valid_sudoku(board)

    def _is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Internal implementation.  
        Validates if a given 9x9 Sudoku board is valid.

        Time Complexity: O(1) — fixed 9x9 board, at most 81 iterations.  
        Space Complexity: O(1) — 27 sets total, each ≤ 9 elements.

        Args:
            board (List[List[str]]): 9x9 Sudoku board, may contain '.' for empty cells.

        Returns:
            bool: True if valid, False otherwise.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                box_index = (i // 3) * 3 + j // 3

                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True
