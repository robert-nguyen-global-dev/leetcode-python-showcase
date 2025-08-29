class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_longest_palindromic_substring()` for actual implementation.
        """
        return self._longest_palindromic_substring(s)

    def _longest_palindromic_substring(self, s: str) -> str:
        """
        Internal implementation.  
        Finds the longest palindromic substring in the given string using
        the Expand Around Center technique.

        For each index, we attempt to expand for both odd-length and even-length
        palindromes, updating the maximum length and starting index when a longer
        palindrome is found.

        Time Complexity: O(n^2) — where n is the length of the string.  
        Space Complexity: O(1) — constant extra space.

        Args:
            s (str): Input string.

        Returns:
            str: The longest palindromic substring.
        """
        if len(s) < 2:
            return s

        start, max_len = 0, 1

        def expand_from_center(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start = left
                    max_len = current_len
                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd-length palindromes
            expand_from_center(i, i)
            # Even-length palindromes
            expand_from_center(i, i + 1)

        return s[start:start + max_len]
