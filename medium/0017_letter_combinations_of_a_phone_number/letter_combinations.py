class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_letter_combinations()` for actual implementation.
        """
        return self._letter_combinations(digits)

    def _letter_combinations(self, digits: str) -> list[str]:
        """
        Internal implementation.  
        Generates all possible letter combinations from a string of digits
        based on the classic phone keypad mapping.

        Uses backtracking to explore all possible combinations.

        Time Complexity: O(3^N * 4^M) — where:
            - N = number of digits mapping to 3 letters (2,3,4,5,6,8)
            - M = number of digits mapping to 4 letters (7,9)

        Space Complexity: O(n) — recursion stack + temporary path storage.

        Args:
            digits (str): String containing digits from 2 to 9.

        Returns:
            list[str]: All possible letter combinations.
        """
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: list[str]):
            if index == len(digits):
                result.append("".join(path))
                return

            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
