from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_remove_duplicates()` for actual implementation.
        """
        return self._remove_duplicates(nums)

    def _remove_duplicates(self, nums: List[int]) -> int:
        """
        Internal implementation.
        Removes duplicates from a sorted integer array in-place and returns the new length,
        such that the first part of the array contains only unique elements in their original order.

        Utilizes a two-pointer strategy: one pointer tracks the position for the next unique element,
        while the other traverses the array — enabling efficient overwrite of duplicates.

        Time Complexity: O(n) — where n is the length of the input array.
        Space Complexity: O(1) — modifies the input list in-place with constant extra space.

        Args:
            nums (List[int]): A list of integers sorted in non-decreasing order.

        Returns:
            int: The length of the updated array containing only unique elements at the front.
        """
        if not nums:
            return 0

        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
