class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_roman_to_int()` for actual implementation.
        """
        return self._roman_to_int(s)

    def _roman_to_int(self, s: str) -> int:
        """
        Internal implementation.
        Converts a Roman numeral string to its corresponding integer value.

        Args:
            s (str): Roman numeral string.

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
