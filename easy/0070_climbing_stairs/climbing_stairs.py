class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_climb_stairs()` for actual implementation.
        """
        return self._climb_stairs(n)

    def _climb_stairs(self, n: int) -> int:
        """
        Internal implementation.
        Computes the number of distinct ways to climb a staircase of `n` steps,
        where at each step, you can climb either 1 or 2 steps.

        This solution uses a bottom-up dynamic programming approach with space optimization.
        It maintains only the last two computed values, similar to calculating Fibonacci numbers.

        Time Complexity: O(n) — iterates through the staircase steps once.
        Space Complexity: O(1) — uses only two variables for rolling computation.

        Args:
            n (int): Total number of steps in the staircase.

        Returns:
            int: Total number of unique ways to reach the top.
        """
        if n <= 2:
            return n

        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr