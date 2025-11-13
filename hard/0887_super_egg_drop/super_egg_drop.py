class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _super_egg_drop() for actual implementation.
        """
        return self._super_egg_drop(k, n)

    def _super_egg_drop(self, k: int, n: int) -> int:
        """
        Internal implementation.  
        Uses optimized dynamic programming based on number of moves.

        Time Complexity: O(k * log n) — grows quickly with moves but far faster than O(k * n²).  
        Space Complexity: O(k) — only need dp array of size k.

        Args:
            k (int): Number of eggs.
            n (int): Number of floors.

        Returns:
            int: Minimum number of moves required to find the critical floor.
        """
        dp = [0] * (k + 1)
        moves = 0

        # Increase moves until dp[k] >= n
        while dp[k] < n:
            moves += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i - 1] + dp[i] + 1

        return moves
