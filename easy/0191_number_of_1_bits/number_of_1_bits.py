class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_hamming_weight()` for actual implementation.
        """
        return self._hamming_weight(n)

    def _hamming_weight(self, n: int) -> int:
        """
        Internal implementation.  
        Counts the number of 1 bits (Hamming weight) in the binary representation of an unsigned integer.

        The key idea is to use the bit manipulation trick `n = n & (n - 1)`, which removes the lowest set bit (rightmost 1)
        from the number `n`. We repeat this until `n` becomes 0. This approach loops exactly k times, where k is the
        number of 1-bits in the input — making it very efficient when `n` has few set bits.

        This technique avoids checking each bit individually, making it faster than iterating through 32 positions.

        Time Complexity: O(k) — where k is the number of 1 bits in `n`.  
        Space Complexity: O(1) — constant extra space.

        Args:
            n (int): An unsigned 32-bit integer.

        Returns:
            int: The number of 1 bits in `n`.
        """
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
