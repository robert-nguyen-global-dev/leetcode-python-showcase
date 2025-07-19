class Solution:
    def isValid(self, s: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_valid()` for actual implementation.
        """
        return self._is_valid(s)

    def _is_valid(self, s: str) -> bool:
        """
        Internal implementation.  
        Checks whether a given string of brackets is valid in terms of proper opening and closing order.

        Uses a stack to track opening brackets and matches each closing bracket accordingly,
        ensuring that every bracket type is closed in the correct sequence and properly nested.

        Time Complexity: O(n) — where n is the length of the input string.  
        Space Complexity: O(n) — in the worst case, all characters are opening brackets stored in the stack.

        Args:
            s (str): Input string consisting only of '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the bracket sequence is valid, False otherwise.
        """
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                # Invalid character
                return False

        return not stack
