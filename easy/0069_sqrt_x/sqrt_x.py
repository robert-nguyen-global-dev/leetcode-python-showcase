class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_binary_search_sqrt()` for actual implementation.
        """
        return self._binary_search_sqrt(x)

    def _binary_search_sqrt(self, x: int) -> int:
        """
        Internal implementation.  
        Uses binary search to compute integer square root.

        Time Complexity: O(log x) — binary search reduces range each step.  
        Space Complexity: O(1) — constant extra space.

        Args:
            x (int): Non-negative integer.

        Returns:
            int: The integer square root of x (floor of real sqrt).
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        result = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
