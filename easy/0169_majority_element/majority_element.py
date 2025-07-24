from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_majority_element()` for actual implementation.
        """
        return self._majority_element(nums)

    def _majority_element(self, nums: List[int]) -> int:
        """
        Internal implementation.  
        Finds the majority element — the element that appears more than ⌊n / 2⌋ times.

        Uses Boyer-Moore Voting Algorithm to find the candidate with linear time and constant space.  
        Maintains a count and a candidate. When the count is zero, a new candidate is chosen.  
        Then iterates through the list again to confirm if the candidate appears more than n/2 times.

        Time Complexity: O(n) — single pass to determine candidate and another to confirm majority.  
        Space Complexity: O(1) — constant space for count and candidate variables.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The majority element.
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Optional verification step (can be removed if guaranteed majority exists)
        if nums.count(candidate) > len(nums) // 2:
            return candidate

        raise ValueError("No majority element found")
