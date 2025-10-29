class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _product_except_self() for actual implementation.
        """
        return self._product_except_self(nums)

    def _product_except_self(self, nums: list[int]) -> list[int]:
        """
        Internal implementation.  
        Using prefix and suffix products.

        Steps:
        1. Create an output array where output[i] stores product of all elements to the left of i.
        2. Then traverse from the right and multiply each element with running suffix product.

        Time Complexity: O(n)  
        Space Complexity: O(1) (excluding output array)

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            List[int]: Product of all elements except self for each index.
        """
        n = len(nums)
        output = [1] * n

        # Step 1: Compute prefix product
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Step 2: Compute suffix product and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
