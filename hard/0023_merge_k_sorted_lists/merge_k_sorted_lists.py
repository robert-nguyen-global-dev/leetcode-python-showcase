from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __lt__(self, other: "ListNode") -> bool:
        """
        Heap requires a comparator. We compare nodes by value.
        """
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _merge_k_lists() for actual implementation.
        """
        return self._merge_k_lists(lists)

    def _merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Internal implementation.  
        Using a min-heap.

        Algorithm:
        - Push first node of each non-empty list into a min-heap.
        - Repeatedly pop the smallest node, append it to output.
        - If popped node has next -> push next into heap.

        Time Complexity: O(N log k)
            N = total number of nodes across all lists
            k = number of lists  
        Space Complexity: O(k) for the heap

        Args:
            lists (List[Optional[ListNode]]): List of sorted linked-lists.

        Returns:
            Optional[ListNode]: Head of the merged sorted linked-list.
        """
        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, head)

        dummy = ListNode()
        tail = dummy

        while min_heap:
            smallest = heapq.heappop(min_heap)
            tail.next = smallest
            tail = tail.next

            if smallest.next:
                heapq.heappush(min_heap, smallest.next)

        return dummy.next
