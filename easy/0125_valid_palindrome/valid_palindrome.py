class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_palindrome()` for actual implementation.
        """
        return self._is_palindrome(s)

    def _is_palindrome(self, s: str) -> bool:
        """
        Internal implementation.  
        Determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

        The function first filters the input string by removing all non-alphanumeric characters
        and converting it to lowercase. It then compares the cleaned string to its reverse
        to check for palindrome property.

        Although a two-pointer approach can achieve the same result using O(1) space, this version prioritizes 
        readability and maintainability, making it ideal for clean code showcases and testability. The trade-off 
        is an additional O(n) space usage for the filtered list.

        Time Complexity: O(n) — where n is the length of the input string.  
        Space Complexity: O(n) — due to the additional space used for the filtered string.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the processed string is a palindrome, False otherwise.
        """
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]
