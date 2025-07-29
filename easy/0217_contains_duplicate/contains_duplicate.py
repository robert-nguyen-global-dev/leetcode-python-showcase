from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_contains_duplicate()` for actual implementation.
        """
        return self._contains_duplicate(nums)

    def _contains_duplicate(self, nums: List[int]) -> bool:
        """
        Internal implementation.  
        Determines if any value appears at least twice in the list.

        This method uses a hash set to track the values seen so far.
        If a number is already in the set, a duplicate has been found.

        This approach provides an efficient check for duplicates with minimal space usage.

        Time Complexity: O(n) — where n is the number of elements in the list.  
        Space Complexity: O(n) — for storing the unique elements in a set.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if any value appears more than once, False otherwise.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
