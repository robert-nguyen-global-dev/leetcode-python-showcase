from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_sliding_window() for actual implementation.
        """
        return self._max_sliding_window(nums, k)

    def _max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        Internal implementation.  
        Using Monotonic Deque.

        Maintains a decreasing deque of indices to track maximums efficiently.

        Time Complexity: O(n) — each element is pushed and popped at most once.  
        Space Complexity: O(k) — size of the deque.

        Args:
            nums (List[int]): Input array of integers.
            k (int): Window size.

        Returns:
            List[int]: List of maximum values for each sliding window.
        """
        if not nums or k == 0:
            return []

        queue = deque()  # store indices of elements, decreasing by value
        result = []

        for i, num in enumerate(nums):
            # Step 1: Remove elements out of window range
            while queue and queue[0] <= i - k:
                queue.popleft()

            # Step 2: Maintain decreasing order
            while queue and nums[queue[-1]] < num:
                queue.pop()

            # Step 3: Add current index
            queue.append(i)

            # Step 4: Add to result once window has size k
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
