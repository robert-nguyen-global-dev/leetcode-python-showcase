class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_title_to_number()` for actual implementation.
        """
        return self._title_to_number(columnTitle)

    def _title_to_number(self, columnTitle: str) -> int:
        """
        Internal implementation.  
        Converts a column title (e.g., "A", "AB", "ZY") into its corresponding Excel column number.

        Treats the title as a base-26 number where 'A' = 1, 'B' = 2, ..., 'Z' = 26.  
        Iterates through each character, updating the result by multiplying the previous result by 26
        and adding the numeric value of the current letter.

        Time Complexity: O(n) — where n is the length of the column title.  
        Space Complexity: O(1) — constant space usage.

        Args:
            columnTitle (str): The Excel-style column title consisting of uppercase English letters.

        Returns:
            int: The corresponding column number.
        """
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
