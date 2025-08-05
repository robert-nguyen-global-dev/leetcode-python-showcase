from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        """
        Precomputes prefix sums such that prefix[i] = sum of nums[0] to nums[i-1].

        Time Complexity: O(n) — where n is the length of the input list.  
        Space Complexity: O(n) — to store prefix sums.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            None
        """
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_sum_range()` for actual implementation.
        """
        return self._sum_range(left, right)
    
    def _sum_range(self, left: int, right: int) -> int:
        """
        Internal implementation.  
        Returns the sum of elements between indices left and right inclusive.

        Time Complexity: O(1) — direct lookup from precomputed prefix sums.  
        Space Complexity: O(1)

        Args:
            left (int): Starting index (inclusive).
            right (int): Ending index (inclusive).

        Returns:
            int: Sum of nums[left] to nums[right].
        """
        return self.prefix[right + 1] - self.prefix[left]
