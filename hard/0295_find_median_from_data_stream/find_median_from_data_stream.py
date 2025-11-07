import heapq


class MedianFinder:
    """
    Data structure to continuously add numbers and retrieve the median efficiently.

    Uses two heaps:
    - max_heap: stores the smaller half (as negative numbers for max-heap simulation)
    - min_heap: stores the larger half
    """

    def __init__(self):
        """Initialize two heaps for median tracking."""
        self.max_heap = []  # max-heap (store as negative)
        self.min_heap = []  # min-heap

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.

        Steps:
        1. Add to max_heap (as negative value).
        2. Move the largest from max_heap to min_heap to maintain order.
        3. Balance heap sizes if necessary.

        Time Complexity: O(log n)
        """
        # Step 1: Add to max_heap
        heapq.heappush(self.max_heap, -num)

        # Step 2: Move top element from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Step 3: Balance heaps
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        """
        Returns the median of all numbers added so far.

        If odd count → top of max_heap.  
        If even count → average of tops from both heaps.

        Time Complexity: O(1)    
        Space Complexity: O(n)
        """
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
