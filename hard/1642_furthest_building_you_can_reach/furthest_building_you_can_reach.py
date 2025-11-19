import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _furthest_building() for actual implementation.
        """
        return self._furthest_building(heights, bricks, ladders)

    def _furthest_building(self, heights, bricks, ladders):
        """
        Internal implementation.  
        Uses greedy strategy with a min-heap to allocate bricks and ladders
        optimally for upward climbs.

        Time Complexity: O(n log n) — heap insertions for climbs.  
        Space Complexity: O(n) — stores climb differences.

        Args:
            heights (List[int]): Heights of buildings.
            bricks (int): Number of bricks available.
            ladders (int): Number of ladders available.

        Returns:
            int: The furthest index that can be reached.
        """
        min_heap = []  # stores all positive climbs

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            # Only care about upward climbs
            if climb > 0:
                heapq.heappush(min_heap, climb)

            # If using too many ladders → use bricks for the smallest climb
            if len(min_heap) > ladders:
                smallest_climb = heapq.heappop(min_heap)
                bricks -= smallest_climb

            # If bricks run out → cannot move further
            if bricks < 0:
                return i

        return len(heights) - 1
