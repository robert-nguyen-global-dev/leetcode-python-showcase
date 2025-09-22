from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _reverse_between() for actual implementation.
        """
        return self._reverse_between(head, left, right)

    def _reverse_between(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        Internal implementation.  
        Reverses the sublist of a linked list between positions left and right.

        Time Complexity: O(n) — single pass through the list.  
        Space Complexity: O(1) — in-place reversal.

        Args:
            head (ListNode): Head of the linked list.
            left (int): Starting position of sublist (1-indexed).
            right (int): Ending position of sublist (1-indexed).

        Returns:
            ListNode: Head of the modified linked list.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Step 1: Move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist between left and right
        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
