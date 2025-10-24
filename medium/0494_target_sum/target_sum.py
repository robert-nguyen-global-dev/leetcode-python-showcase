class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_target_sum_ways() for actual implementation.
        """
        return self._find_target_sum_ways(nums, target)

    def _find_target_sum_ways(self, nums: list[int], target: int) -> int:
        """
        Internal implementation.  
        Using Dynamic Programming (subset-sum transformation).

        Transforms the problem into counting subsets with a given sum:
            sum(P) = (sum(nums) + target) / 2

        dp[i] = number of ways to get sum i using available numbers.

        Time Complexity: O(n * sum(nums))  
        Space Complexity: O(sum(nums))

        Args:
            nums (List[int]): List of non-negative integers.
            target (int): Target sum after assigning + or -.

        Returns:
            int: Number of different ways to assign symbols to reach target.
        """
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0

        subset_sum = (total + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # one way to make sum = 0 (choose nothing)

        for num in nums:
            # iterate backward to avoid reuse
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]
