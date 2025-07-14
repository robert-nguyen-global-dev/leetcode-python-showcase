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
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_merge_two_lists()` for actual implementation.
        """
        return self._merge_two_lists(list1, list2)

    def _merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.
        Merges two sorted linked lists and returns the merged sorted list.

        Performs in-place merging by reusing nodes to achieve linear time and constant space.

        Time Complexity: O(m + n) — where m and n are the lengths of the input lists.
        Space Complexity: O(1) — uses constant extra space by reusing existing nodes.

        Args:
            list1 (Optional[ListNode]): First sorted linked list.
            list2 (Optional[ListNode]): Second sorted linked list.

        Returns:
            Optional[ListNode]: Merged sorted linked list.
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
