from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Entry point with LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_can_construct()` for actual implementation.
        """
        return self._can_construct(ransomNote, magazine)

    def _can_construct(self, ransomNote: str, magazine: str) -> bool:
        """
        Internal implementation.  
        Determines if ransomNote can be constructed from magazine.

        Approach:
        - Use Counter to count occurrences of each character in magazine.
        - Iterate through ransomNote, checking if each character exists
          in the magazine counter with a positive count.
        - Decrement the count when a character is used.
        - If any character is missing or depleted, return False.
        - If all characters are matched, return True.

        Time Complexity: O(m + n) — where m = len(ransomNote), n = len(magazine)
        Space Complexity: O(1) — because the character set is limited to lowercase English letters.

        Explanation:
        - Counting takes O(n) time.
        - Iteration through ransomNote takes O(m) time.
        - We store at most 26 keys in the counter, so extra space is constant.
        
        Args:
            ransomNote (str): The note to construct.
            magazine (str): The available characters.

        Returns:
            bool: True if ransomNote can be constructed, False otherwise.
        """
        magazine_count = Counter(magazine)
        
        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1
        
        return True