class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_product_subarray() for actual implementation.
        """
        return self._max_product_subarray(nums)

    def _max_product_subarray(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Uses dynamic programming with tracking current max and min products.

        Time Complexity: O(n)  
        Space Complexity: O(1)

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            int: Maximum product of any contiguous subarray.
        """
        if not nums:
            return 0

        cur_max = cur_min = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, num * cur_max)
            cur_min = min(num, num * cur_min)
            ans = max(ans, cur_max)

        return ans
