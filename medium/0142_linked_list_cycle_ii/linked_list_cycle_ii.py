from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _detectCycle() for actual implementation.
        """
        return self._detectCycle(head)

    def _detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.  
        Using Floyd's Tortoise and Hare.

        Time Complexity: O(n).  
        Space Complexity: O(1).

        Args:
            head (ListNode): Head of the linked list.

        Returns:
            ListNode: Node where the cycle begins, or None if no cycle exists.
        """
        if not head or not head.next:
            return None

        slow, fast = head, head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find entry point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
