from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_peak_element() for actual implementation.
        """
        return self._find_peak_element(nums)

    def _find_peak_element(self, nums: List[int]) -> int:
        """
        Internal implementation.  
        Uses binary search to locate a peak element.

        Time Complexity: O(log n)  
        Space Complexity: O(1)

        Args:
            nums (List[int]): Input array.

        Returns:
            int: Index of any peak element.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1  # peak is in the right half
            else:
                right = mid  # peak is in the left half (including mid)

        return left
