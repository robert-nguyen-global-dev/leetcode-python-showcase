from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_anagrams() for actual implementation.
        """
        return self._find_anagrams(s, p)

    def _find_anagrams(self, s: str, p: str) -> List[int]:
        """
        Internal implementation.  
        Uses sliding window + frequency arrays to detect anagrams.

        Time Complexity: O(n) — n = len(s), each char visited at most twice.  
        Space Complexity: O(1) — frequency arrays of size 26.

        Args:
            s (str): The main string.
            p (str): The pattern string to find anagrams of.

        Returns:
            List[int]: Starting indices of anagrams of p in s.
        """
        res = []
        len_s, len_p = len(s), len(p)

        if len_p > len_s:
            return res

        # Step 1: Count frequency of p and initial window in s
        freq_p = [0] * 26
        freq_window = [0] * 26

        for ch in p:
            freq_p[ord(ch) - ord('a')] += 1
        for ch in s[:len_p]:
            freq_window[ord(ch) - ord('a')] += 1

        # Step 2: Sliding window
        if freq_window == freq_p:
            res.append(0)

        for i in range(len_p, len_s):
            # Remove leftmost char
            freq_window[ord(s[i - len_p]) - ord('a')] -= 1
            # Add new char
            freq_window[ord(s[i]) - ord('a')] += 1

            if freq_window == freq_p:
                res.append(i - len_p + 1)

        return res
