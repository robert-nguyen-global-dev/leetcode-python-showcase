from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_two_sum()` for actual implementation.
        """
        return self._two_sum(nums, target)

    def _two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Internal implementation.
        Finds two indices such that the numbers at those indices add up to the given target value.

        Uses a hash map to store previously visited numbers and their indices while traversing the list.
        For each number, checks if the complement (target - current) exists in the map.

        Time Complexity: O(n) — where n is the number of elements in the list.
        Space Complexity: O(n) — additional space used for the hash map to track complements.

        Args:
            nums (List[int]): List of integers.
            target (int): Target sum to find.

        Returns:
            List[int]: Indices of the two numbers such that they add up to the target.
        """
        num_to_index = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[number] = index

        return []
