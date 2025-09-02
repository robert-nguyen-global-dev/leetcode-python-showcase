from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_remove_nth_from_end()` for actual implementation.
        """
        return self._remove_nth_from_end(head, n)

    def _remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Internal implementation.  
        Removes the nth node from the end of a singly linked list using two pointers.

        Uses a dummy node to simplify edge cases (e.g., removing the head).

        Time Complexity: O(n) — traverse the list once.  
        Space Complexity: O(1) — uses constant extra space.

        Args:
            head (ListNode): Head of the linked list.
            n (int): Index from the end (1-based).

        Returns:
            ListNode: The head of the modified list.
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first ahead by n + 1 steps
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Delete the target node
        second.next = second.next.next

        return dummy.next
