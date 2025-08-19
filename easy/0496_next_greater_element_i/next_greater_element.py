from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_next_greater_element()` for actual implementation.
        """
        return self._next_greater_element(nums1, nums2)

    def _next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Internal implementation.  
        Finds the next greater element for each number in nums1 from nums2.

        Approach:
        - Use a monotonic decreasing stack while iterating nums2.
        - For each number in nums2:
            - While stack is not empty and current number > stack top:
                - Pop stack and map it to current number (next greater element).
        - For remaining numbers in stack, map them to -1.
        - Build the result for nums1 from the computed mapping.

        Time Complexity: O(m + n) — where m = len(nums1), n = len(nums2).  
        Space Complexity: O(n) — to store the hashmap and stack.

        Args:
            nums1 (List[int]): Subset of nums2.
            nums2 (List[int]): Superset array containing nums1.

        Returns:
            List[int]: List of next greater elements corresponding to nums1.
        """
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        # Remaining elements in stack do not have a next greater
        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]
