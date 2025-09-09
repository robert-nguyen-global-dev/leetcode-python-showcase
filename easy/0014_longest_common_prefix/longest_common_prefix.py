from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_longest_common_prefix()` for actual implementation.
        """
        return self._longest_common_prefix(strs)

    def _longest_common_prefix(self, strs: List[str]) -> str:
        """
        Internal implementation.  
        Finds the longest common prefix among a list of strings.

        Approach:
        - Take the first string as reference.
        - For each character index, compare with other strings.
        - Stop when mismatch or index exceeds any string length.

        Time Complexity: O(n x m) — n = number of strings, m = min string length.  
        Space Complexity: O(1) — only uses a few variables.

        Args:
            strs (List[str]): List of strings.

        Returns:
            str: The longest common prefix.
        """
        if not strs:
            return ""

        # Find the shortest string to limit our search range
        min_length = min(len(s) for s in strs)
        prefix = []

        for i in range(min_length):
            current_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != current_char:
                    return "".join(prefix)
            prefix.append(current_char)

        return "".join(prefix)
