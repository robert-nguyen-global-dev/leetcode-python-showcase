from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_search_rotated_sorted_array()` for actual implementation.
        """
        return self._search_rotated_sorted_array(nums, target)

    def _search_rotated_sorted_array(self, nums: List[int], target: int) -> int:
        """
        Internal implementation.  
        Searches for a target value in a rotated sorted array using binary search.

        Time Complexity: O(log n) — modified binary search.  
        Space Complexity: O(1) — only uses two pointer.

        Args:
            nums (List[int]): Rotated sorted array of integers.
            target (int): Target value to search.

        Returns:
            int: Index of target if found, else -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
