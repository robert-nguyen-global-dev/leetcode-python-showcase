import math

class Solution:
    def numSquares(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _num_squares() for actual implementation.
        """
        return self._num_squares(n)

    def _num_squares(self, n: int) -> int:
        """
        Internal implementation.  
        Using Dynamic Programming (bottom-up).

        dp[i] = min number of perfect squares that sum up to i.  
        dp[0] = 0

        Transition:
            dp[i] = min(dp[i - j*j] + 1) for all j where j*j <= i

        Time Complexity: O(n * sqrt(n))  
        Space Complexity: O(n)

        Args:
            n (int): Target number.

        Returns:
            int: Minimum count of perfect squares that sum to n.
        """
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
