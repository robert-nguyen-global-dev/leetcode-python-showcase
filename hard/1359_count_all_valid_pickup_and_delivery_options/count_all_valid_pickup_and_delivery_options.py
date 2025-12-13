class Solution:
    def countOrders(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _count_orders() for actual implementation.
        """
        return self._count_orders(n)

    def _count_orders(self, n: int) -> int:
        """
        Internal implementation.  
        Counting all valid pickup and delivery sequences.

        Approach:
            - Math / Combinatorics solution.
            - The number of valid sequences for n orders is:
                ans = Π_{i=1..n} (2i - 1) * i
            - Multiply under modulo 1e9+7 to avoid overflow.
            - Uses simple iterative computation.

        Time Complexity: O(n) — Single pass multiplication.  
        Space Complexity: O(1) — Constant space.

        Args:
            n (int): Number of pickup/delivery pairs.

        Returns:
            int: Total valid sequences modulo 1e9+7.
        """
        MOD = 10**9 + 7
        result = 1

        for i in range(1, n + 1):
            result = (result * (2 * i - 1) * i) % MOD

        return result
