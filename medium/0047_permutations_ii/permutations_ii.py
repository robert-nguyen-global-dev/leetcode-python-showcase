from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _permute_unique() for actual implementation.
        """
        return self._permute_unique(nums)

    def _permute_unique(self, nums: List[int]) -> List[List[int]]:
        """
        Internal implementation.  
        Generates all unique permutations using backtracking.

        Time Complexity: O(n * n!) — generates all unique permutations.  
        Space Complexity: O(n) — recursion stack + visited array.

        Args:
            nums (List[int]): Input list possibly containing duplicates.

        Returns:
            List[List[int]]: All unique permutations.
        """
        nums.sort()
        res = []
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited[i] = False

        backtrack([])
        return res
