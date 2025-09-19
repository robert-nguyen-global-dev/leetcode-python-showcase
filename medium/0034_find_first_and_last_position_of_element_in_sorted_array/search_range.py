from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _search_range() for actual implementation.
        """
        return self._search_range(nums, target)

    def _search_range(self, nums: List[int], target: int) -> List[int]:
        """
        Internal implementation.  
        Uses binary search to find first and last position of target.

        Time Complexity: O(log n)  
        Space Complexity: O(1)

        Args:
            nums (List[int]): Sorted integer array.
            target (int): Target value to search.

        Returns:
            List[int]: [first_index, last_index] or [-1, -1] if not found.
        """
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # continue search left
                    else:
                        left = mid + 1   # continue search right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        first = find_bound(is_first=True)
        if first == -1:
            return [-1, -1]
        last = find_bound(is_first=False)
        
        return [first, last]
