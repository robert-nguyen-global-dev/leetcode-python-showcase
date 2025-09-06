from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_combination_sum_ii()` for actual implementation.
        """
        return self._combination_sum_ii(candidates, target)

    def _combination_sum_ii(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Internal implementation.  
        Finds all unique combinations where numbers sum to target.  
        Each number can be used at most once.

        Approach:
        1. Sort candidates → makes duplicate skipping easier.
        2. Use backtracking:
            - If total == target → add current combination.
            - If total > target → prune path.
            - Otherwise, recurse with next index.
        3. Skip duplicate candidates to avoid redundant combinations.

        Time Complexity: O(2^N) in worst case (all subsets explored)  
        Space Complexity: O(N) for recursion depth.

        Args:
            candidates (List[int]): List of positive integers.
            target (int): Desired sum.

        Returns:
            List[List[int]]: All unique combinations.
        """
        candidates.sort()
        result = []

        def backtrack(start: int, current: List[int], total: int):
            # Base case: found valid combination
            if total == target:
                result.append(current.copy())
                return

            # Explore numbers starting from 'start'
            for i in range(start, len(candidates)):
                # Skip duplicate numbers
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Prune if adding current number exceeds target
                if total + candidates[i] > target:
                    break

                # Choose the current number
                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
