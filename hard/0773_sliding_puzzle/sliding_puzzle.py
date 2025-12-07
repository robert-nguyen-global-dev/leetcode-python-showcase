from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _sliding_puzzle() for actual implementation.
        """
        return self._sliding_puzzle(board)

    def _sliding_puzzle(self, board: List[List[int]]) -> int:
        """
        Internal implementation.  
        Using BFS to find minimum moves.

        Time Complexity: O(720) = O(6!) maximum states  
        Space Complexity: O(720)

        Args:
            board (List[List[int]]): 2x3 initial board configuration

        Returns:
            int: minimum number of moves to reach target, -1 if impossible
        """
        target = "123450"
        start = "".join(str(num) for row in board for num in row)

        # neighbor indices for swap with 0 in 1D string representation
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [2, 4]
        }

        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero_idx = state.index('0')
            for nei in neighbors[zero_idx]:
                lst = list(state)
                lst[zero_idx], lst[nei] = lst[nei], lst[zero_idx]
                next_state = "".join(lst)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
        return -1
