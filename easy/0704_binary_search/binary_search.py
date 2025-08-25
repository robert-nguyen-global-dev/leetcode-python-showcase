class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_binary_search()` for actual implementation.
        """
        return self._binary_search(nums, target)

    def _binary_search(self, nums: list[int], target: int) -> int:
        """
        Internal implementation.  
        Finds the index of `target` in a sorted list `nums` using binary search.

        Approach:
        - Initialize `left` and `right` pointers.
        - While `left <= right`:
            - Calculate `mid = (left + right) // 2`.
            - If `nums[mid]` equals `target`, return `mid`.
            - If `nums[mid]` < `target`, move `left` to `mid + 1`.
            - Otherwise, move `right` to `mid - 1`.
        - If not found, return -1.

        Time Complexity: O(log n) — binary search halves the search space each iteration.  
        Space Complexity: O(1) — constant extra space.

        Args:
            nums (list[int]): Sorted list of integers.
            target (int): Target integer to search for.

        Returns:
            int: Index of `target` if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
