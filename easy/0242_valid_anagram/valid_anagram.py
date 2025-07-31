class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_anagram()` for actual implementation.
        """
        return self._is_anagram(s, t)

    def _is_anagram(self, s: str, t: str) -> bool:
        """
        Internal implementation.  
        Determines whether two strings are anagrams of each other.

        This method counts the frequency of each character in both strings
        and compares the frequency maps.

        Time Complexity: O(n) — where n is the length of the strings (assuming same length).  
        Space Complexity: O(1) — because the character set is limited to lowercase English letters.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        if len(s) != len(t):
            return False
        
        if not s.isascii() or not t.isascii():
            return False

        count = [0] * 26  # Assuming only lowercase English letters
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1

        return all(value == 0 for value in count)
