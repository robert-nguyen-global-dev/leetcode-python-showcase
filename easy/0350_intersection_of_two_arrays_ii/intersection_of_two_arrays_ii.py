from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_intersect()` for actual implementation.
        """
        return self._intersect(nums1, nums2)

    def _intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Internal implementation.  
        Returns the intersection of two arrays, where each element in the result
        should appear as many times as it shows in both arrays.

        This method counts the frequency of elements in the smaller array
        and then iterates over the larger array to build the intersection.

        Time Complexity: O(m + n) — where m and n are the lengths of the two arrays.  
        Space Complexity: O(min(m, n)) — because we store frequencies of the smaller array.

        Args:
            nums1 (List[int]): The first list of integers.
            nums2 (List[int]): The second list of integers.

        Returns:
            List[int]: The intersection list with duplicates allowed.
        """
        # Always iterate over the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        freq_map = Counter(nums1)
        result = []

        for num in nums2:
            if freq_map.get(num, 0) > 0:
                result.append(num)
                freq_map[num] -= 1

        return result
