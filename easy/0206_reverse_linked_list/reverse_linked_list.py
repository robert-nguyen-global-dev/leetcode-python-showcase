from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_reverse_list()` for actual implementation.
        """
        return self._reverse_list(head)

    def _reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.  
        Reverses a singly linked list in-place using iterative approach.

        It iterates through the linked list, changing the next pointers of each node
        to point to the previous node, effectively reversing the list.

        Time Complexity: O(n) — where n is the number of nodes in the linked list.  
        Space Complexity: O(1) — no extra space used; in-place reversal.

        Args:
            head (ListNode | None): The head of the linked list.

        Returns:
            ListNode | None: The new head of the reversed linked list.
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
