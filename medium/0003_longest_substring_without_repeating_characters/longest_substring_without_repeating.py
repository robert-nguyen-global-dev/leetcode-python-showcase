class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_length_of_longest_substring()` for actual implementation.
        """
        return self._length_of_longest_substring(s)

    def _length_of_longest_substring(self, s: str) -> int:
        """
        Internal implementation.  
        Finds the length of the longest substring without repeating characters.

        Uses the sliding window technique combined with a hash map to store
        the last seen index of each character. When a duplicate is found,
        moves the left pointer to maintain a valid substring.

        Time Complexity: O(n) — where n is the length of the string.  
        Space Complexity: O(k) — where k is the size of the character set.

        Args:
            s (str): The input string consisting of ASCII characters.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        char_index = {}
        left = max_len = 0

        for right, char in enumerate(s):
            # If the char is repeated and within the current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
