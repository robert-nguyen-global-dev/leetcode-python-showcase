from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _judge_point_24() for actual implementation.
        """
        return self._judge_point_24(cards)

    def _judge_point_24(self, cards: List[int]) -> bool:
        """
        Internal implementation.  
        Uses backtracking to try all combinations of arithmetic operations.

        Time Complexity: O(4^n * n!) — explores all pairings and operations.  
        Space Complexity: O(n) — recursion depth proportional to number of cards.

        Args:
            cards (List[int]): List of 4 integers in [1, 9].

        Returns:
            bool: True if 24 can be achieved, False otherwise.
        """
        EPSILON = 1e-6  # floating-point tolerance

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    next_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    # Generate all possible results of nums[i] and nums[j]
                    for val in self._apply_operations(nums[i], nums[j]):
                        next_nums.append(val)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

            return False

        return dfs([float(c) for c in cards])

    def _apply_operations(self, a: float, b: float) -> List[float]:
        """
        Helper function to apply all valid operations between two numbers.  
        Avoids division by zero.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            List[float]: Results of applying all possible operations.
        """
        results = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:
            results.append(a / b)
        if abs(a) > 1e-6:
            results.append(b / a)
        return results
