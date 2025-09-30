from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _exist() for actual implementation.
        """
        return self._exist(board, word)

    def _exist(self, board: List[List[str]], word: str) -> bool:
        """
        Internal implementation.  
        Using DFS backtracking.

        Time Complexity: O(N * 3^L) — N = the number of cell in board, L = the length of word.  
        Space Complexity: O(L) — recursion depth.

        Args:
            board (List[List[str]]): 2D grid of characters.
            word (str): Word to search in the grid.

        Returns:
            bool: True if word exists in the grid, False otherwise.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[idx]):
                return False

            # Mark as visited
            temp, board[r][c] = board[r][c], "#"

            # Explore 4 directions
            res = (dfs(r + 1, c, idx + 1) or
                   dfs(r - 1, c, idx + 1) or
                   dfs(r, c + 1, idx + 1) or
                   dfs(r, c - 1, idx + 1))

            # Restore after backtracking
            board[r][c] = temp
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
