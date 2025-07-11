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
