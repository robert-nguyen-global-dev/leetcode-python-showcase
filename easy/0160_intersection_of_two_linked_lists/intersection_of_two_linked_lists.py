from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_get_intersection_node()` for actual implementation.
        """
        return self._get_intersection_node(headA, headB)

    def _get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Internal implementation.  
        Finds the intersection node of two singly linked lists using two-pointer technique.

        The key idea is to use two pointers that traverse each list. When either pointer reaches
        the end, it switches to the head of the other list. This ensures both pointers traverse
        equal lengths (m + n), and they meet at the intersection node if it exists.

        If no intersection exists, both pointers eventually become None.

        Time Complexity: O(m + n) — where m and n are the lengths of the two linked lists.  
        Space Complexity: O(1) — constant space; no additional data structures used.

        Args:
            headA (ListNode): Head of the first linked list.
            headB (ListNode): Head of the second linked list.

        Returns:
            ListNode | None: The intersection node, or None if the lists do not intersect.
        """
        if not headA or not headB:
            return None

        currentA, currentB = headA, headB

        while currentA != currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA

        return currentA
