from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_is_palindrome()` for actual implementation.
        """
        return self._is_palindrome(head)

    def _is_palindrome(self, head: Optional[ListNode]) -> bool:
        """
        Internal implementation.  
        Checks whether the given singly linked list is a palindrome.

        It uses the fast-slow pointer approach to find the middle,
        reverses the second half in-place, and compares both halves.

        Time Complexity: O(n) — where n is the number of nodes in the linked list.  
        Space Complexity: O(1) — only constant extra space is used.

        Args:
            head (Optional[ListNode]): The head node of the singly linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """
        if not head or not head.next:
            return True

        # Find middle (slow will point to midpoint)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare first and reversed second halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
