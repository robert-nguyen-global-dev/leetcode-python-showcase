class Solution:
    def addDigits(self, num: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _add_digits() for actual implementation.
        """
        return self._add_digits(num)

    def _add_digits(self, num: int) -> int:
        """
        Internal implementation.  
        Calculates the digital root using constant-time formula.

        The digital root is the result of repeatedly summing the digits of a number
        until a single-digit number is obtained.

        Time Complexity: O(1)  
        Space Complexity: O(1)

        Args:
            num (int): A non-negative integer

        Returns:
            int: The single-digit result of repeated digit addition
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
