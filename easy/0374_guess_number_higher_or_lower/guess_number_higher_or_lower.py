# The guess API is already defined in LeetCode:
# def guess(num: int) -> int:

guess = None  # This line enables monkeypatching

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_guess_number()` for actual implementation.
        """
        return self._guess_number(n)

    def _guess_number(self, n: int) -> int:
        """
        Internal implementation.  
        Uses binary search to guess the correct number within the range [1, n].

        Time Complexity: O(log n) — binary search halves the search space each iteration.  
        Space Complexity: O(1) — only constant extra space is used.

        Explanation:
        - We use binary search because the API `guess(num)` allows comparison
          to check whether our guess is too high, too low, or correct.
        - This approach minimizes the number of calls to the API.
        - The search range is progressively reduced until we find the correct number.

        Args:
            n (int): The upper bound of the range (inclusive).

        Returns:
            int: The number selected by the `guess` API.
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)  # Provided by LeetCode

            if result == 0:
                return mid
            elif result < 0:  # target is smaller
                right = mid - 1
            else:  # target is larger
                left = mid + 1

        return -1  # Should never reach here if the API is correct
