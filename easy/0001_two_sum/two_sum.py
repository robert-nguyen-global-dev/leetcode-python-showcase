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
        Find two indices such that the numbers at those indices add up to the target.

        Solves the problem using a HashMap to achieve linear time complexity.
        
        Time Complexity: O(n)
        Space Complexity: O(n) — uses a HashMap to store visited elements.

        Args:
            nums (List[int]): List of integers.
            target (int): Target sum.

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
