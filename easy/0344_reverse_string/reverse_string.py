from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_reverse_string()` for actual implementation.
        """
        self._reverse_string(s)

    def _reverse_string(self, s: List[str]) -> None:
        """
        Internal implementation.  
        Reverses the input list of characters in-place.

        This method uses two pointers: one starting from the beginning,
        and one from the end. It swaps characters until the pointers meet.

        Time Complexity: O(n) — where n is the length of the input list.  
        Space Complexity: O(1) — the reversal is done in-place with no extra memory.

        Args:
            s (List[str]): The list of characters to be reversed in-place.

        Returns:
            None
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
