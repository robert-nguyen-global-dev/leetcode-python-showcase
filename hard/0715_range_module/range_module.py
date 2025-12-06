from typing import List
import bisect


class RangeModule:
    def __init__(self):
        """
        Initializes the RangeModule with an empty list of intervals.
        """
        # intervals: list of [start, end), sorted by start, non-overlapping
        self.intervals: List[List[int]] = []

    def addRange(self, left: int, right: int) -> None:
        """
        Add [left, right) to the active ranges, merging overlapping intervals.

        Time Complexity: O(n) worst-case (merge)  
        Space Complexity: O(n)
        """
        new_intervals: List[List[int]] = []
        placed = False
        for start, end in self.intervals:
            if end < left:
                new_intervals.append([start, end])
            elif start > right:
                if not placed:
                    new_intervals.append([left, right])
                    placed = True
                new_intervals.append([start, end])
            else:  # overlap
                left = min(left, start)
                right = max(right, end)
        if not placed:
            new_intervals.append([left, right])
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        """
        Returns True if [left, right) is completely covered by active intervals.
        Uses binary search for efficient query.

        Time Complexity: O(log n)
        """
        intervals = self.intervals
        i = bisect.bisect_right(intervals, [left, float('inf')]) - 1
        if i >= 0 and intervals[i][0] <= left and intervals[i][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        """
        Remove [left, right) from active intervals, splitting intervals if necessary.

        Time Complexity: O(n)
        """
        new_intervals: List[List[int]] = []
        for start, end in self.intervals:
            if end <= left or start >= right:
                # no overlap
                new_intervals.append([start, end])
            else:
                # overlap: may need left part
                if start < left:
                    new_intervals.append([start, left])
                if end > right:
                    new_intervals.append([right, end])
        self.intervals = new_intervals
