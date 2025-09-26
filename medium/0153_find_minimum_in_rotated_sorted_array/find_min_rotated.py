class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_min() for actual implementation.
        """
        return self._find_min(nums)

    def _find_min(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Binary search for minimum element in rotated sorted array.

        Time Complexity: O(log n)  
        Space Complexity: O(1)

        Args:
            nums (list[int]): Rotated sorted array without duplicates.

        Returns:
            int: Minimum element in array.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # Min nằm bên phải
                left = mid + 1
            else:
                # Min nằm bên trái hoặc là mid
                right = mid

        return nums[left]
