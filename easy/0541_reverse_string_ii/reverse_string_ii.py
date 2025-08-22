class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_reverse_str()` for actual implementation.
        """
        return self._reverse_str(s, k)

    def _reverse_str(self, s: str, k: int) -> str:
        """
        Internal implementation.  
        Reverses the first k characters for every 2k characters in the string.

        Approach:
        - Use slicing and step 2k.
        - For each segment starting at index i:
            - Reverse s[i:i+k]
            - Keep s[i+k:i+2k] unchanged.
        - Append to result list and join at the end.

        Time Complexity: O(n) — each character is processed once.  
        Space Complexity: O(n) — stores the result in a separate list.

        Args:
            s (str): Input string.
            k (int): Number of characters to reverse in each 2k block.

        Returns:
            str: The transformed string after applying the reversal rules.
        """
        result = []
        for i in range(0, len(s), 2 * k):
            result.append(s[i:i + k][::-1])  # Reverse first k chars
            result.append(s[i + k:i + 2 * k])  # Keep next k chars unchanged
        return ''.join(result)
