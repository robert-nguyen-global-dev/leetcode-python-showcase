class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _check_inclusion() for actual implementation.
        """
        return self._check_inclusion(s1, s2)

    def _check_inclusion(self, s1: str, s2: str) -> bool:
        """
        Internal implementation.  
        Uses sliding window + frequency arrays to check if s2 contains a permutation of s1.

        Time Complexity: O(n) — n = len(s2), each char visited at most twice.  
        Space Complexity: O(1) — frequency arrays of size 26.

        Args:
            s1 (str): Pattern string.
            s2 (str): Main string.

        Returns:
            bool: True if any permutation of s1 is a substring of s2, else False.
        """
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        # Step 1: Count frequencies for s1 and first window in s2
        freq_s1 = [0] * 26
        freq_window = [0] * 26

        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1
        for ch in s2[:len_s1]:
            freq_window[ord(ch) - ord('a')] += 1

        # Step 2: Sliding window
        if freq_window == freq_s1:
            return True

        for i in range(len_s1, len_s2):
            # Remove leftmost char
            freq_window[ord(s2[i - len_s1]) - ord('a')] -= 1
            # Add new char
            freq_window[ord(s2[i]) - ord('a')] += 1

            if freq_window == freq_s1:
                return True

        return False
