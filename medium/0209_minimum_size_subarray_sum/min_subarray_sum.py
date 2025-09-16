from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _min_sub_array_len() for actual implementation.
        """
        return self._min_sub_array_len(target, nums)

    def _min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """
        Internal implementation.  
        Uses sliding window technique to find minimal length subarray sum ≥ target.

        Time Complexity: O(n) — each element visited at most twice.  
        Space Complexity: O(1).

        Args:
            target (int): The target sum to achieve.
            nums (List[int]): List of positive integers.

        Returns:
            int: Minimal length of subarray with sum ≥ target, or 0 if none exist.
        """
        n = len(nums)
        left = 0
        total = 0
        min_len = float("inf")

        for right in range(n):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len
