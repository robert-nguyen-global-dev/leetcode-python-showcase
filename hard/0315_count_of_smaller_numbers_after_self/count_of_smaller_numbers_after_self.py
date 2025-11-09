from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _count_smaller_merge_sort() for actual implementation.
        """
        return self._count_smaller_merge_sort(nums)

    def _count_smaller_merge_sort(self, nums: List[int]) -> List[int]:
        """
        Internal implementation.  
        Uses modified merge sort to count smaller elements after each number.

        Time Complexity: O(n log n) — divide and merge each level.  
        Space Complexity: O(n) — auxiliary arrays.

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            List[int]: List where counts[i] = number of smaller elements to the right of nums[i].
        """
        n = len(nums)
        result = [0] * n
        indexed_nums = list(enumerate(nums))  # [(index, value)]

        def merge_sort(start: int, end: int):
            if end - start <= 1:
                return

            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            # Merge phase with counting
            temp = []
            i, j = start, mid
            right_count = 0

            while i < mid and j < end:
                if indexed_nums[j][1] < indexed_nums[i][1]:
                    right_count += 1
                    temp.append(indexed_nums[j])
                    j += 1
                else:
                    result[indexed_nums[i][0]] += right_count
                    temp.append(indexed_nums[i])
                    i += 1

            while i < mid:
                result[indexed_nums[i][0]] += right_count
                temp.append(indexed_nums[i])
                i += 1

            while j < end:
                temp.append(indexed_nums[j])
                j += 1

            # Copy back
            for k in range(len(temp)):
                indexed_nums[start + k] = temp[k]

        merge_sort(0, n)
        return result
