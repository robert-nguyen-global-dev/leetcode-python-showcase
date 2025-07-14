from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_remove_duplicates()` for actual implementation.
        """
        return self._remove_duplicates(nums)

    def _remove_duplicates(self, nums: List[int]) -> int:
        """
        Internal implementation.
        Removes duplicates from sorted array in-place and returns the new length.

        Uses two pointers to overwrite duplicates while preserving order,
        achieving linear time and constant space.

        Time Complexity: O(n) — where n is the length of the input array.
        Space Complexity: O(1) — modifies the array in-place without extra memory.

        Args:
            nums (List[int]): A sorted list of integers.

        Returns:
            int: The length of the modified list with unique elements at the front.
        """
        if not nums:
            return 0

        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
