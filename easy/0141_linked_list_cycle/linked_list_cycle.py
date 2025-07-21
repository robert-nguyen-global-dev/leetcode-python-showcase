from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method signature.

        Delegates to `_has_cycle()` for actual logic implementation.
        """
        return self._has_cycle(head)

    def _has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Internal implementation.  
        Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

        The algorithm uses two pointers moving at different speeds. If there is a cycle,
        the fast pointer will eventually meet the slow pointer. If the fast pointer reaches
        the end of the list, then there is no cycle.

        This approach avoids using extra memory like a visited set, making it highly efficient
        in both time and space. It's ideal for large linked lists and low-memory environments.

        Time Complexity: O(n) — where n is the number of nodes in the list.  
        Space Complexity: O(1) — uses constant space for two pointers.

        Args:
            head (ListNode): The head of the singly linked list.

        Returns:
            bool: True if there is a cycle in the list, False otherwise.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False
