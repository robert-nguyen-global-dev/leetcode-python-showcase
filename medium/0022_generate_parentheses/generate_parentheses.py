from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _generate_parenthesis() for actual implementation.
        """
        return self._generate_parenthesis(n)

    def _generate_parenthesis(self, n: int) -> List[str]:
        """
        Internal implementation.  
        Uses backtracking to generate all valid parentheses strings.

        Time Complexity: O(4^n / sqrt(n)) — Catalan number growth.  
        Space Complexity: O(n) recursion depth.

        Args:
            n (int): Number of parentheses pairs.

        Returns:
            List[str]: All valid parentheses combinations.
        """
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result