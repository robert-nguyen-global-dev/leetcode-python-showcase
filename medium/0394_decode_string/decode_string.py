class Solution:
    def decodeString(self, s: str) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _decodeString() for actual implementation.
        """
        return self._decodeString(s)

    def _decodeString(self, s: str) -> str:
        """
        Internal implementation.  
        Using stack-based decoding.

        Time Complexity: O(n) — each char processed once.  
        Space Complexity: O(n) — stack usage for nested structures.

        Args:
            s (str): Encoded string.

        Returns:
            str: Decoded string.
        """
        stack = []
        current_str = ""
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)  # handle multi-digit numbers
            elif ch == "[":
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif ch == "]":
                prev_str, num = stack.pop()
                current_str = prev_str + num * current_str
            else:
                current_str += ch

        return current_str
