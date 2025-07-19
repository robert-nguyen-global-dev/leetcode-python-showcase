class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_roman_to_int()` for actual implementation.
        """
        return self._roman_to_int(s)

    def _roman_to_int(self, s: str) -> int:
        """
        Internal implementation.  
        Converts a Roman numeral string to its corresponding integer by parsing symbols and applying subtraction rules.

        Uses a fixed lookup table to map Roman characters to values and iterates through the string,
        adjusting the total based on whether the current symbol is smaller than the next (e.g., IV = 4).

        Time Complexity: O(n) — where n is the length of the input string.  
        Space Complexity: O(1) — constant space used for the lookup table.

        Args:
            s (str): Roman numeral string containing characters 'I', 'V', 'X', 'L', 'C', 'D', and 'M'.

        Returns:
            int: The integer value corresponding to the Roman numeral.
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total
