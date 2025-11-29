from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_envelopes() for actual implementation.
        """
        return self._max_envelopes(envelopes)

    def _max_envelopes(self, envelopes: List[List[int]]) -> int:
        """
        Internal implementation.  
        Computes the maximum number of envelopes that can be nested.

        Steps:
        1. Sort by width ASC, height DESC (to avoid invalid LIS cases).
        2. Extract heights.
        3. Compute LIS on heights with binary search.

        Time Complexity: O(n log n).  
        Space Complexity: O(n)

        Args:
            envelopes (List[List[int]]): List of [width, height] pairs.

        Returns:
            int: Maximum number of envelopes that can be nested.
        """
        if not envelopes:
            return 0

        # Sort: width ASC, height DESC
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract only heights
        heights = [h for _, h in envelopes]

        # LIS using binary search
        lis: List[int] = []
        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)
