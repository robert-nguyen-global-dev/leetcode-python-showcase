class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _first_unique_char() for actual implementation.
        """
        return self._first_unique_char(s)

    def _first_unique_char(self, s: str) -> int:
        """
        Internal implementation.  
        Uses counting array (26 letters) to track frequencies.

        Time Complexity: O(n) — two passes over the string.  
        Space Complexity: O(1) — fixed array of 26 counts.

        Args:
            s (str): Input string containing only lowercase letters.

        Returns:
            int: Index of the first unique character, or -1 if none exist.
        """
        # Step 1: Count frequencies
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Step 2: Find first char with count = 1
        for i, ch in enumerate(s):
            if freq[ord(ch) - ord('a')] == 1:
                return i

        return -1
