class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_bitwise_sum()` for actual implementation.
        """
        return self._bitwise_sum(a, b)

    def _bitwise_sum(self, a: int, b: int) -> int:
        """
        Internal implementation.  
        Computes the sum of two integers without '+' or '-'.

        Time Complexity: O(1) — at most 32 iterations for 32-bit integer.  
        Space Complexity: O(1).

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            int: Sum of a and b.
        """
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        # Convert from unsigned to signed
        return a if a <= INT_MAX else ~(a ^ MASK)
