class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _rob_circular() for actual implementation.
        """
        return self._rob_circular(nums)

    def _rob_circular(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Handles circular adjacency by solving two linear rob problems:
        - Case 1: Exclude last house (rob from 0 to n-2)
        - Case 2: Exclude first house (rob from 1 to n-1)

        Time Complexity: O(n)  
        Space Complexity: O(1)

        Args:
            nums (List[int]): List of money in each circularly arranged house.

        Returns:
            int: Maximum money that can be robbed without robbing adjacent houses.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr: list[int]) -> int:
            prev2, prev1 = 0, 0
            for money in arr:
                current = max(prev1, prev2 + money)
                prev2, prev1 = prev1, current
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
