from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: object):
        """Allow == comparison for testing linked lists."""
        if not isinstance(other, ListNode):
            return False
            
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
            
        return a is None and b is None

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_merge_two_lists()` for actual implementation.
        """
        return self._merge_two_lists(list1, list2)

    def _merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.
        Merges two sorted singly linked lists into one sorted list by reusing existing nodes,
        without allocating new list nodes.

        Traverses both input lists simultaneously, attaching the smaller current node to the result list,
        ensuring all elements remain in non-decreasing order while minimizing memory usage.

        Time Complexity: O(m + n) — where m and n are the lengths of the input lists.
        Space Complexity: O(1) — merges in-place by reassigning existing pointers without extra allocation.

        Args:
            list1 (Optional[ListNode]): First input linked list, sorted in non-decreasing order.
            list2 (Optional[ListNode]): Second input linked list, also sorted in non-decreasing order.

        Returns:
            Optional[ListNode]: The head node of the merged sorted linked list.
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        
        return dummy.next
