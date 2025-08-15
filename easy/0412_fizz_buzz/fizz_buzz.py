class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_fizz_buzz()` for actual implementation.
        """
        return self._fizz_buzz(n)

    def _fizz_buzz(self, n: int) -> list[str]:
        """
        Internal implementation.  
        Generates the FizzBuzz sequence for numbers from 1 to n.

        For each number:
        - If divisible by both 3 and 5, add "FizzBuzz".
        - If divisible by 3 only, add "Fizz".
        - If divisible by 5 only, add "Buzz".
        - Otherwise, add the string representation of the number.

        Time Complexity: O(n) — we process each number once.  
        Space Complexity: O(n) — for storing the result list.

        Args:
            n (int): The upper limit of the sequence (inclusive).

        Returns:
            list[str]: The generated FizzBuzz sequence.
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
