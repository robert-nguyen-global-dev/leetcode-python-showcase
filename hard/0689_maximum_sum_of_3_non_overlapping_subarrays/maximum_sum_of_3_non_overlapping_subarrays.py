from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_sum_of_three_subarrays() for actual implementation.
        """
        return self._max_sum_of_three_subarrays(nums, k)

    def _max_sum_of_three_subarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Internal implementation.

        Steps:
        1. Compute window_sum[i] = sum(nums[i:i+k]) for all valid i.
        2. Compute best_left[i]: index of max window in [0..i] (ties -> smaller index).
        3. Compute best_right[i]: index of max window in [i..n-k] (ties -> smaller index).
        4. Iterate middle window start m from k to n - 2k:
           compute total = window_sum[best_left[m-1]] + window_sum[m] + window_sum[best_right[m+k]]
           update answer when total is greater.

        Time Complexity: O(n)  
        Space Complexity: O(n)

        Args:
            nums (List[int]): input array of integers.
            k (int): size of each subarray.

        Returns:
            List[int]: starting indices of the 3 subarrays with maximum total sum.
        """
        n = len(nums)
        if n < 3 * k:
            return []

        # Step 1: window_sum
        window_sum = [sum(nums[i:i+k]) for i in range(n-k+1)]

        # Step 2: left_max
        left = [0]*len(window_sum)
        best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best

        # Step 3: right_max
        right = [0]*len(window_sum)
        best = len(window_sum)-1
        for i in range(len(window_sum)-1, -1, -1):
            if window_sum[i] >= window_sum[best]:   # tie → lexicographically smallest
                best = i
            right[i] = best

        # Step 4: iterate middle
        res = None
        max_total = -1
        for j in range(k, len(window_sum)-k):
            i = left[j-k]
            l = right[j+k]
            total = window_sum[i]+window_sum[j]+window_sum[l]
            if total > max_total:
                max_total = total
                res = [i,j,l]
        return res
