from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _min_interval() for actual implementation.
        """
        return self._min_interval(intervals, queries)

    def _min_interval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Internal implementation.  
        Uses sorting + min-heap to maintain intervals that cover each query.

        Algorithm Summary:
        - Sort intervals by start.
        - Sort queries while keeping original indices.
        - Use a min-heap storing (interval_length, end) for all intervals that start <= query.
        - Pop intervals from heap whose end < query (not covering the query).
        - The top of the heap is the smallest interval that covers the query.

        Time Complexity: O([n + q] log n) - heap operations and sorting.  
        Space Complexity: O(n) - heap + data structures

        Args:
            intervals (List[List[int]]): List of [start, end] intervals.
            queries (List[int]): Query points.

        Returns:
            List[int]: For each query, the minimum interval length covering it,
            or -1 if not found.
        """
        import heapq

        # Step 1: Sort intervals by start
        intervals.sort(key=lambda seg: seg[0])

        # Step 2: Sort queries with their original indices
        indexed_queries = sorted((q, idx) for idx, q in enumerate(queries))

        # Min-heap storing (interval_length, interval_end)
        min_heap = []

        # Pointer to intervals
        interval_index = 0
        total_intervals = len(intervals)

        # Initialize result array
        result = [-1] * len(queries)

        # Step 3: Process queries in sorted order
        for query_value, original_index in indexed_queries:

            # Add all intervals where start <= query_value
            while interval_index < total_intervals and intervals[interval_index][0] <= query_value:
                start, end = intervals[interval_index]
                interval_length = end - start + 1
                heapq.heappush(min_heap, (interval_length, end))
                interval_index += 1

            # Remove intervals that do not cover the query (end < query_value)
            while min_heap and min_heap[0][1] < query_value:
                heapq.heappop(min_heap)

            # The top of heap is the smallest interval covering the query
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result
