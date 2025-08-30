from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_max_container_area()` for actual implementation.
        """
        return self._max_container_area(height)

    def _max_container_area(self, height: List[int]) -> int:
        """
        Internal implementation.  
        Finds the maximum area of water that can be contained
        using the Two Pointers technique.

        Time Complexity: O(n) — single pass through the array.  
        Space Complexity: O(1) — constant extra space.

        Args:
            height (List[int]): List of non-negative integers representing vertical lines.

        Returns:
            int: Maximum area of water that can be contained.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            # Move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
