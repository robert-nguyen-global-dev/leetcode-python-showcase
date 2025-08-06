class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_power_of_three()` for actual implementation.
        """
        return self._is_power_of_three(n)

    def _is_power_of_three(self, n: int) -> bool:
        """
        Internal implementation.  
        Determines whether a given integer is a power of three.

        This method uses the fact that the maximum power of 3 that fits in a 32-bit
        signed integer [1, 2^{31}-1] is 3^19 = 1162261467. If n is a divisor of 1162261467,
        then n must be a power of 3.

        Time Complexity: O(1) — only one modulo operation and one comparison.  
        Space Complexity: O(1) — no extra space is used beyond constant variables.

        Args:
            n (int): The input number to be checked.

        Returns:
            bool: True if n is a power of three, False otherwise.
        """
        return n > 0 and 1162261467 % n == 0
