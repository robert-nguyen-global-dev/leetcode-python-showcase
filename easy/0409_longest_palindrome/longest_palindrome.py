class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_longest_palindrome()` for actual implementation.
        """
        return self._longest_palindrome(s)

    def _longest_palindrome(self, s: str) -> int:
        """
        Internal implementation.  
        Finds the length of the longest palindrome that can be built with the letters of the given string.

        This method counts character frequencies and uses the counts to determine the
        maximum palindrome length. For each character, we can use the largest even
        count, and we can use exactly one odd character in the center if available.

        Time Complexity: O(n) — where n is the length of the string.  
        Space Complexity: O(1) — because the character set is limited to ASCII letters.

        Args:
            s (str): The input string consisting of ASCII letters.

        Returns:
            int: The length of the longest palindrome that can be built.
        """
        if not s.isascii():
            return 0

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        length = 0
        odd_found = False
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        return length + 1 if odd_found else length
