class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _rob_house() for actual implementation.
        """
        return self._rob_house(nums)

    def _rob_house(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Uses bottom-up dynamic programming to compute max robbery amount.

        Time Complexity: O(n)  
        Space Complexity: O(1)

        Args:
            nums (List[int]): List representing money in each house.

        Returns:
            int: Maximum money that can be robbed without robbing adjacent houses.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current

        return prev1
