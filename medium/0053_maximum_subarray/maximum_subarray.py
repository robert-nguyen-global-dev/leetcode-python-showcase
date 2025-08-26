class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_max_subarray()` for actual implementation.
        """
        return self._max_subarray(nums)

    def _max_subarray(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Finds the maximum subarray sum using Kadane's Algorithm.

        Approach:
        - Use dynamic programming / greedy approach.
        - Keep track of:
            * current_sum: best sum ending at current index.
            * max_sum: best sum found so far.
        - At each step:
            * current_sum = max(nums[i], current_sum + nums[i])
            * max_sum = max(max_sum, current_sum)

        Time Complexity: O(n) — iterate through nums once.  
        Space Complexity: O(1) — only uses constant extra space.

        Args:
            nums (List[int]): Input integer array.

        Returns:
            int: Maximum sum of any contiguous subarray.
        """
        if not nums:
            return 0

        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
