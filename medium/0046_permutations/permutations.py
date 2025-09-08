from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_permute()` for actual implementation.
        """
        return self._permute(nums)

    def _permute(self, nums: List[int]) -> List[List[int]]:
        """
        Internal implementation.  
        Uses backtracking to generate all possible permutations.

        Approach:
        - Use DFS + backtracking.
        - At each recursion level, pick one number that hasn't been used yet.
        - Once the current path reaches length `n`, append it to the result.

        Time Complexity: O(n * n!) — n! permutations, and copying each takes O(n).  
        Space Complexity: O(n) — recursion depth and temporary path.

        Args:
            nums (List[int]): List of unique integers.

        Returns:
            List[List[int]]: All possible permutations.
        """
        result = []
        used = [False] * len(nums)

        def backtrack(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Un-choose (backtrack)
                path.pop()
                used[i] = False

        backtrack([])
        return result
