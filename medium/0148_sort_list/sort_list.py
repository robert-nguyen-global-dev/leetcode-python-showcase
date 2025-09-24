from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _sort_list() for actual implementation.
        """
        return self._sort_list(head)

    def _sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.  
        Sorts a linked list using merge sort.

        Time Complexity: O(n log n) — divide & merge.  
        Space Complexity: O(log n) — recursion stack depth.

        Args:
            head (ListNode): Head of the linked list.

        Returns:
            ListNode: Head of the sorted linked list.
        """
        if not head or not head.next:
            return head

        # Step 1: Split list into two halves
        mid = self._get_middle(head)
        right_head = mid.next
        mid.next = None

        # Step 2: Sort both halves
        left_sorted = self._sort_list(head)
        right_sorted = self._sort_list(right_head)

        # Step 3: Merge sorted halves
        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, head: ListNode) -> ListNode:
        """
        Finds the middle node of the linked list (for splitting).
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists.
        """
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next
