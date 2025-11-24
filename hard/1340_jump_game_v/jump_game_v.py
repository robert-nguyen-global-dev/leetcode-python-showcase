from typing import List
from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_jumps() for actual implementation.
        """
        return self._max_jumps(arr, d)

    def _max_jumps(self, arr: List[int], d: int) -> int:
        """
        Internal implementation.  
        Dynamic Programming based on processing indices by increasing value.

        dp[i] = maximum jumps starting from index i.
        For each index, explore up to d steps left/right until:
        - the boundary of array, or
        - an element >= arr[i] appears (blocking further movement).

        Time Complexity: O(n * d)  
        Space Complexity: O(n)

        Args:
            arr (List[int]): Input array representing heights.
            d (int): Maximum distance allowed per jump.

        Returns:
            int: Maximum number of jumps achievable from any starting index.
        """
        n = len(arr)
        if n == 0:
            return 0

        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            best = 1  # at least stay at itself

            # explore left: i-1 down to i-d (inclusive), but stop if hit >= arr[i]
            # range stop is exclusive, so we use i-d-1; also ensure stop >= -1
            left_stop = max(i - d - 1, -1)
            for left in range(i - 1, left_stop, -1):
                # left will never be negative because left_stop >= -1,
                # but if left becomes -1 it's excluded by range (since stop is -1),
                # so left always in [0..i-1]
                if arr[left] >= arr[i]:
                    break
                best = max(best, 1 + dfs(left))

            # explore right: i+1 up to i+d (inclusive)
            # range stop should be i+d+1, but also not exceed n
            right_stop = min(i + d + 1, n)
            for right in range(i + 1, right_stop):
                if arr[right] >= arr[i]:
                    break
                best = max(best, 1 + dfs(right))

            return best

        return max(dfs(i) for i in range(n))
