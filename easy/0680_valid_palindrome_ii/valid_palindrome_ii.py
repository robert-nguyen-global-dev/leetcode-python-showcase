class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_valid_palindrome()` for actual implementation.
        """
        return self._valid_palindrome(s)

    def _valid_palindrome(self, s: str) -> bool:
        """
        Internal implementation.  
        Checks if the string `s` can be a palindrome after deleting at most one character.

        Approach:
        - Use two pointers (`left` and `right`).
        - While characters at both ends are equal, move inward.
        - If a mismatch occurs:
            - Option 1: Skip `s[left]` and check if remaining substring is palindrome.
            - Option 2: Skip `s[right]` and check if remaining substring is palindrome.
        - Return True if either option forms a palindrome.

        Time Complexity: O(n) — each character visited at most twice.  
        Space Complexity: O(1) — constant extra space.

        Args:
            s (str): Input string.

        Returns:
            bool: True if `s` can be palindrome after deleting at most one char, else False.
        """
        def is_palindrome(sub: str, l: int, r: int) -> bool:
            """Helper function to check if substring s[l:r+1] is palindrome."""
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try removing either left or right character
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
