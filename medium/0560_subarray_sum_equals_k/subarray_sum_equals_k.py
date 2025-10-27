class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _subarray_sum() for actual implementation.
        """
        return self._subarray_sum(nums, k)

    def _subarray_sum(self, nums: list[int], k: int) -> int:
        """
        Internal implementation.  
        Using Prefix Sum and Hash Map.

        prefix_count[sum] = number of occurrences of prefix_sum.  
        For each curr_sum, check how many times (curr_sum - k) has appeared.

        Time Complexity: O(n)  
        Space Complexity: O(n)

        Args:
            nums (List[int]): Input array of integers.
            k (int): Target sum value.

        Returns:
            int: Number of continuous subarrays whose sum equals k.
        """
        prefix_count = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            # Step 1: Check if there's a prefix that leads to sum = k
            if (curr_sum - k) in prefix_count:
                count += prefix_count[curr_sum - k]

            # Step 2: Update prefix_count for current sum
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return count
