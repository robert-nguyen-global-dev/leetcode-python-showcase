from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_merge_sorted_array()` for actual implementation.  
        Modifies nums1 in-place.
        """
        self._merge_sorted_array(nums1, m, nums2, n)

    def _merge_sorted_array(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Internal implementation.  
        Merges two sorted arrays into one sorted array in-place by modifying `nums1`.

        The algorithm starts from the end of both arrays to avoid overwriting elements in `nums1`.  
        By placing the largest elements at the end and working backward, it ensures correctness with constant extra space.

        Time Complexity: O(m + n) — where m is the number of valid elements in nums1, and n is the number of elements in nums2.  
        Space Complexity: O(1) — performs the merge in-place using pointers.

        Args:
            nums1 (List[int]): First array of length m + n, where the first m elements are valid and the rest are placeholders.
            m (int): Number of valid elements in nums1.
            nums2 (List[int]): Second array containing n sorted elements.
            n (int): Number of elements in nums2.

        Returns:
            None
        """
        pointer_nums1 = m - 1
        pointer_nums2 = n - 1
        insert_position = m + n - 1

        while pointer_nums1 >= 0 and pointer_nums2 >= 0:
            if nums1[pointer_nums1] > nums2[pointer_nums2]:
                nums1[insert_position] = nums1[pointer_nums1]
                pointer_nums1 -= 1
            else:
                nums1[insert_position] = nums2[pointer_nums2]
                pointer_nums2 -= 1
            insert_position -= 1

        # Only need to copy remaining nums2 if any
        while pointer_nums2 >= 0:
            nums1[insert_position] = nums2[pointer_nums2]
            pointer_nums2 -= 1
            insert_position -= 1

