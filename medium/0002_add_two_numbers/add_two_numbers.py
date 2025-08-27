from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_add_two_numbers()` for actual implementation.
        """
        return self._add_two_numbers(l1, l2)

    def _add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Internal implementation.  
        Adds two numbers represented as linked lists in reverse order.

        Approach:
        - Use two pointers to traverse both linked lists simultaneously.
        - Maintain a carry variable to handle sums greater than 9.
        - Construct a new linked list using a dummy head for convenience.

        Time Complexity: O(max(m, n)) — where m and n are lengths of l1 and l2.  
        Space Complexity: O(max(m, n)) — for the output linked list.

        Args:
            l1 (Optional[ListNode]): Head of the first linked list.
            l2 (Optional[ListNode]): Head of the second linked list.

        Returns:
            Optional[ListNode]: Head of the resulting linked list.
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
