class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _combination_sum4() for actual implementation.
        """
        return self._combination_sum4(nums, target)

    def _combination_sum4(self, nums: list[int], target: int) -> int:
        """
        Internal implementation.  
        Using Dynamic Programming (count ordered combinations).

        dp[i] = number of ordered combinations that sum to i.  
        dp[0] = 1 (base case: one way to make 0)

        Transition:
            dp[i] += dp[i - num] for each num in nums if i >= num

        Time Complexity: O(n * target)  
        Space Complexity: O(target)

        Args:
            nums (List[int]): Distinct positive integers.
            target (int): Target sum.

        Returns:
            int: Number of ordered combinations that add up to target.
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]
