from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_move_zeroes()` for actual implementation.
        """
        self._move_zeroes(nums)

    def _move_zeroes(self, nums: List[int]) -> None:
        """
        Internal implementation.  
        Moves all zeroes in the list to the end while maintaining the order of non-zero elements.  
        This function modifies the list in-place.

        Approach:
        - Use two-pointer technique:
            - One pointer `insert_pos` to track the position for non-zero elements.
            - Iterate through the list. For each non-zero element, place it at `insert_pos`.
            - After all non-zero elements are moved, fill the rest of the array with zeros.

        Time Complexity: O(n) — where n is the length of the array.  
        Space Complexity: O(1) — in-place with no extra data structures.

        Args:
            nums (List[int]): The list of integers to be modified in-place.

        Returns:
            None
        """
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0
