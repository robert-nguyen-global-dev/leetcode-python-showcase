from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _copy_random_list() for actual implementation.
        """
        return self._copy_random_list(head)

    def _copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        """
        Internal implementation.  
        Creates a deep copy of a linked list with random pointers.

        Time Complexity: O(n) — traverse list 3 times.  
        Space Complexity: O(1) — in-place interweaving approach.

        Args:
            head (Node): Head of the original linked list.

        Returns:
            Node: Head of the deep-copied linked list.
        """
        if not head:
            return None

        # Step 1: Insert copied nodes interleaved with original nodes
        current = head
        while current:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next

        # Step 2: Assign random pointers for the copies
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied lists
        dummy = Node(0)
        copy_current = dummy
        current = head
        while current:
            copy = current.next
            current.next = copy.next
            copy_current.next = copy
            copy_current = copy
            current = current.next

        return dummy.next
