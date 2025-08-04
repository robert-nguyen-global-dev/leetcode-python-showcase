# The isBadVersion API is defined globally and injected during testing

isBadVersion = None  # This line enables monkeypatching
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _first_bad_version() for actual implementation.
        """
        return self._first_bad_version(n)

    def _first_bad_version(self, n: int) -> int:
        """
        Internal implementation.  
        Uses binary search to find the first bad version.

        Time Complexity: O(log n) — because we halve the search range each time.  
        Space Complexity: O(1) — only constant extra variables used.

        Args:
            n (int): Total number of versions.

        Returns:
            int: The version number of the first bad version.
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):  # this function is injected externally
                right = mid
            else:
                left = mid + 1
        return left
