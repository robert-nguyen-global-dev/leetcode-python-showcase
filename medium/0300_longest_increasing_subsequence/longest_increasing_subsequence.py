from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _length_of_lis() for actual implementation.
        """
        return self._length_of_lis(nums)

    def _length_of_lis(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Uses patience sorting idea with binary search.

        Time Complexity: O(n log n)  
        Space Complexity: O(n)

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            int: Length of the longest strictly increasing subsequence.
        """
        if not nums:
            return 0

        tails = []

        for num in nums:
            # Find insertion index in tails
            idx = bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)
