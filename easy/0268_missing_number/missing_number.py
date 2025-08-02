from typing import List


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_missing_number()` for actual implementation.
        """
        return self._missing_number(nums)

    def _missing_number(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Finds the missing number in the range [0, n] using XOR.

        This algorithm takes advantage of the property:
        a ^ a = 0 and a ^ 0 = a.

        By XORing all indices and all numbers, all matched pairs cancel out,
        leaving the missing number as the result.

        Time Complexity: O(n) — where n is the number of elements in the list.  
        Space Complexity: O(1) — constant space used for XOR accumulators.

        Args:
            nums (list[int]): List of n unique numbers from range [0, n] with one missing.

        Returns:
            int: The missing number in the range.
        """
        n = len(nums)
        xor_total = 0
        xor_nums = 0

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor_total ^= i

        # XOR all elements in the array
        for num in nums:
            xor_nums ^= num

        return xor_total ^ xor_nums
