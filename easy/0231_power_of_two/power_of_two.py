class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_power_of_two()` for actual implementation.
        """
        return self._is_power_of_two(n)

    def _is_power_of_two(self, n: int) -> bool:
        """
        Internal implementation.  
        Checks if `n` is a power of two.

        Approach:
        - Power of two numbers have only one '1' in their binary representation.
        - Use bit trick: n & (n-1) == 0 ensures only one bit is set.

        Time Complexity: O(1)  
        Space Complexity: O(1)

        Args:
            n (int): Integer to check.

        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        return n > 0 and (n & (n - 1)) == 0
