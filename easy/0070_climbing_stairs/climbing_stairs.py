class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_climb_stairs()` for actual implementation.
        """
        return self._climb_stairs(n)

    def _climb_stairs(self, n: int) -> int:
        """
        Internal implementation.
        Calculates the number of distinct ways to climb to the top of a staircase
        with `n` steps, where each time you can climb 1 or 2 steps.

        Uses bottom-up dynamic programming with rolling variables to achieve linear time and constant space.

        Time Complexity: O(n) — iterates once through n steps.
        Space Complexity: O(1) — uses a fixed number of variables without extra data structures.

        Args:
            n (int): Number of steps.

        Returns:
            int: Number of distinct ways to reach the top.
        """
        if n <= 2:
            return n

        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr