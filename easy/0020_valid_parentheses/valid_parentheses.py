class Solution:
    def isValid(self, s: str) -> bool:
        """
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_valid()` for actual implementation.
        """
        return self._is_valid(s)

    def _is_valid(self, s: str) -> bool:
        """
        Internal implementation.
        Checks whether the given string of parentheses is valid.

        A string is valid if all types of brackets are closed in the correct order.

        Args:
            s (str): Input string containing only '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the string is valid, False otherwise.
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
