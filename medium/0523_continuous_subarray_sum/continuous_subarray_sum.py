class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _check_subarray_sum() for actual implementation.
        """
        return self._check_subarray_sum(nums, k)

    def _check_subarray_sum(self, nums: list[int], k: int) -> bool:
        """
        Internal implementation.  
        Using Prefix Sum with modulo tracking.

        Idea:
        - If (prefix_sum[j] - prefix_sum[i]) % k == 0 → subarray (i+1..j) divisible by k.
        - Store earliest index of each modulo value in mod_index map.
        - When a modulo repeats and the subarray length ≥ 2 → return True.

        Time Complexity: O(n)  
        Space Complexity: O(min(n, k))

        Args:
            nums (List[int]): List of non-negative integers.
            k (int): Divisor to check divisibility.

        Returns:
            bool: True if such subarray exists, otherwise False.
        """
        mod_index = {0: -1}  # handle subarray starting from index 0
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k if k != 0 else prefix_sum  # avoid div by zero

            # Step 1: If mod already seen, check distance
            if mod in mod_index:
                if i - mod_index[mod] >= 2:
                    return True
            else:
                # Step 2: Record first occurrence of mod
                mod_index[mod] = i

        return False
