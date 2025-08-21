class Solution:
    def fib(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_fib()` for actual implementation.
        """
        return self._fib(n)

    def _fib(self, n: int) -> int:
        """
        Internal implementation.  
        Computes the n-th Fibonacci number using bottom-up DP with O(1) space.

        Approach:
        - Handle base cases: F(0)=0, F(1)=1.
        - Use two variables `a` and `b` to track the last two Fibonacci numbers.
        - Iteratively compute F(i) until reaching n.

        Time Complexity: O(n) — single pass from 2 to n.  
        Space Complexity: O(1) — only stores two variables.

        Args:
            n (int): Index of Fibonacci number to compute.

        Returns:
            int: The n-th Fibonacci number.
        """
        if n < 2:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
