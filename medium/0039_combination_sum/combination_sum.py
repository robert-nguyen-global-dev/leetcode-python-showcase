from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_combination_sum()` for actual implementation.
        """
        return self._combination_sum(candidates, target)

    def _combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Internal implementation.  
        Finds all unique combinations of candidates that sum up to target.

        Approach:  
        - Use backtracking to explore all possible combinations.
        - At each recursion:
            * If target == 0 → found a valid combination.
            * If target < 0 → stop exploring.
            * Else, choose a number and recurse.
        - Avoid duplicates by starting from the current index.   

        Time Complexity: O(N^(T/M))  
            N = number of candidates  
            T = target  
            M = smallest candidate  
            Worst case: target/M levels, N branching factor.

        Space Complexity: O(T/M) → recursion depth.

        Args:
            candidates (List[int]): List of positive integers.
            target (int): Desired sum.

        Returns:
            List[List[int]]: All unique combinations.
        """
        result = []

        def backtrack(start: int, current: List[int], total: int):
            # Base case: valid combination
            if total == target:
                result.append(current.copy())
                return

            # If sum exceeds target, prune this path
            if total > target:
                return

            # Explore further numbers
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # Reuse same number
                current.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
