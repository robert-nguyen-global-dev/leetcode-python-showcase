class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_find_the_difference()` for actual implementation.
        """
        return self._find_the_difference(s, t)

    def _find_the_difference(self, s: str, t: str) -> str:
        """
        Internal implementation.  
        Finds the extra character in string `t` that is not present in string `s`.

        This method uses the XOR operation to find the difference efficiently.  
        The XOR of all characters from both strings will result in the extra character.

        Time Complexity: O(n) — where n is the length of the strings (assuming same length).  
        Space Complexity: O(1) — because no additional data structures are used.

        Args:
            s (str): The original string.
            t (str): The modified string with one extra character.

        Returns:
            str: The extra character present in `t` but not in `s`.
        """
        xor_result = 0
        for char in s + t:
            xor_result ^= ord(char)
        return chr(xor_result)
