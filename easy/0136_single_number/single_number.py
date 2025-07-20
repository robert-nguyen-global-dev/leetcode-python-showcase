class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_single_number()` for actual implementation.
        """
        return self._single_number(nums)

    def _single_number(self, nums: list[int]) -> int:
        """
        Internal implementation.  
        Finds the single number in a list where every other element appears exactly twice.

        Uses bitwise XOR to cancel out duplicates efficiently. The XOR of two identical
        numbers is 0, and the XOR of any number with 0 is the number itself. By XORing
        all elements, duplicates are eliminated, leaving only the unique number.

        This approach avoids the need for extra memory (like hash maps or sets), making
        it suitable for large inputs and low-memory environments.

        Time Complexity: O(n) — where n is the number of elements in the list.  
        Space Complexity: O(1) — constant space; only one variable is used.

        Args:
            nums (List[int]): List of integers where each element appears twice except one.

        Returns:
            int: The single number that appears only once.
        """
        result = 0
        for num in nums:
            result ^= num
        return result
