from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _subsets() for actual implementation.
        """
        return self._subsets(nums)

    def _subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Internal implementation.  
        Generates all subsets using backtracking.

        Time Complexity: O(n * 2^n) — each element is either chosen or not.  
        Space Complexity: O(n) — recursion stack.

        Args:
            nums (List[int]): Input list of distinct integers.

        Returns:
            List[List[int]]: All possible subsets.
        """
        res = []

        def backtrack(start, path):
            res.append(path[:])  # Save current subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
