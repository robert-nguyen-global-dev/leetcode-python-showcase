from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_jump_game_ii()` for actual implementation.
        """
        return self._jump_game_ii(nums)

    def _jump_game_ii(self, nums: List[int]) -> int:
        """
        Internal implementation.  
        Uses a greedy approach to find the minimum number of jumps.

        Approach:
        - Keep track of the farthest point we can reach so far.
        - Use a sliding window `[start, end]` representing the current jump range.
        - When we reach the end of the window, we increase `jumps`
          and set a new window based on `farthest`.

        Time Complexity: O(n) — one pass through the array.  
        Space Complexity: O(1) — only constant extra variables.

        Args:
            nums (List[int]): Array of non-negative integers.

        Returns:
            int: Minimum number of jumps to reach the last index.
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # When we reach the end of the current jump range
            if i == end:
                jumps += 1
                end = farthest

                # Early stopping if we can already reach the last index
                if end >= n - 1:
                    break

        return jumps
