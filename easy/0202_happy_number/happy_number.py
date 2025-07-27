class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_happy()` for actual implementation.
        """
        return self._is_happy(n)

    def _is_happy(self, n: int) -> bool:
        """
        Internal implementation.  
        Determines whether a number is a "happy number" using Floyd's Cycle Detection Algorithm.

        A happy number is defined as a number that eventually reaches 1 when repeatedly replaced by the 
        sum of the squares of its digits. If the process falls into a cycle that excludes 1,
        the number is not considered happy.

        Floyd's Cycle Detection is used to detect loops by maintaining a slow and a fast pointer.
        If a cycle exists and the number is not happy, the slow and fast pointers will eventually meet.

        Time Complexity: O(log n) — Each iteration reduces the number's magnitude via digit square sum.  
        Space Complexity: O(1) — No extra space used except variables.

        Args:
            n (int): The number to evaluate.

        Returns:
            bool: True if the number is happy, False otherwise.
        """
        def get_next(number: int) -> int:
            total = 0
            while number:
                digit = number % 10
                total += digit * digit
                number //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
