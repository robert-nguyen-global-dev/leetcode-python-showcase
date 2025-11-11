import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _schedule_course() for actual implementation.
        """
        return self._schedule_course(courses)

    def _schedule_course(self, courses: List[List[int]]) -> int:
        """
        Internal implementation.  
        Uses greedy strategy with a max heap to keep track of selected courses.

        Time Complexity: O(n log n) — sorting + heap operations.  
        Space Complexity: O(n) — storing durations in the heap.

        Args:
            courses (List[List[int]]): Each course represented as [duration, lastDay].

        Returns:
            int: Maximum number of courses that can be taken.
        """
        # Step 1: Sort courses by their lastDay (deadline)
        courses.sort(key=lambda x: x[1])

        max_heap = []  # store durations as negative values for max-heap
        current_time = 0

        # Step 2: Iterate through sorted courses
        for duration, last_day in courses:
            if current_time + duration <= last_day:
                # Can take this course
                heapq.heappush(max_heap, -duration)
                current_time += duration
            elif max_heap and -max_heap[0] > duration:
                # Replace the longest course with the current one
                current_time += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)

        return len(max_heap)
