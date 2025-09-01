from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_three_sum()` for actual implementation.
        """
        return self._three_sum(nums)

    def _three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Internal implementation.  
        Finds all unique triplets in the array which sum up to zero.

        Time Complexity: O(n^2) — outer loop O(n) + two-pointer scan O(n).  
        Space Complexity: O(1) — ignoring the result storage.

        Args:
            nums (List[int]): List of integers, can contain duplicates.

        Returns:
            List[List[int]]: List of unique triplets where a + b + c = 0.
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # Skip duplicate numbers for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the current number is greater than 0, break (no valid triplet possible)
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward after processing
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
