from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_three_sum_closest()` for actual implementation.
        """
        return self._three_sum_closest(nums, target)

    def _three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Internal implementation.  
        Finds three integers in nums such that the sum is closest to target.

        Time Complexity: O(n^2) — outer loop O(n) + two-pointer scan O(n).  
        Space Complexity: O(1).

        Args:
            nums (List[int]): List of integers.
            target (int): Target sum.

        Returns:
            int: The sum of the triplet closest to target.
        """
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
