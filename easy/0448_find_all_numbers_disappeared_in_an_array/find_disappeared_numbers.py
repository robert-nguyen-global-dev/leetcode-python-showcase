class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_find_disappeared_numbers()` for actual implementation.
        """
        return self._find_disappeared_numbers(nums)

    def _find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        """
        Internal implementation.  
        Finds all numbers that do not appear in the array `nums`.

        Approach:
        - Iterate through the array and mark the index corresponding to the value as negative.
        - After marking, iterate again; indices with positive values correspond to missing numbers.

        Time Complexity: O(n) — we scan the array twice.  
        Space Complexity: O(1) — in-place marking (ignoring output list).

        Args:
            nums (list[int]): The input array where 1 <= nums[i] <= n.

        Returns:
            list[int]: The list of missing numbers.
        """
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [i + 1 for i, val in enumerate(nums) if val > 0]
