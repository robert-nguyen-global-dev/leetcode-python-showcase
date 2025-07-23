import unittest
from intersection_of_two_linked_lists import ListNode, Solution


# 🧪 Helper to build linked lists with optional intersection
def build_intersecting_lists(common: list[int], listA: list[int], listB: list[int]) -> tuple[ListNode, ListNode, ListNode]:
    """
    Builds two linked lists that optionally intersect at a common tail segment.

    Args:
        common (list[int]): The intersecting tail node values.
        listA (list[int]): Values before the intersection in list A.
        listB (list[int]): Values before the intersection in list B.

    Returns:
        (headA, headB, intersection_node)
    """
    def build_list(values):
        head = current = None
        for val in reversed(values):
            node = ListNode(val, current)
            current = node
        return current

    common_head = build_list(common) if common else None

    def build_with_tail(values, tail):
        head = current = None
        for val in reversed(values):
            node = ListNode(val, current)
            current = node
        if current:
            last = current
            while last.next:
                last = last.next
            last.next = tail
            return current
        else:
            return tail

    headA = build_with_tail(listA, common_head)
    headB = build_with_tail(listB, common_head)
    return headA, headB, common_head


# 🧪 Unit tests for internal logic `_get_intersection_node()`
class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersection_exists(self):
        headA, headB, intersect = build_intersecting_lists([8, 4, 5], [4, 1], [5, 6, 1])
        self.assertIs(self.solution._get_intersection_node(headA, headB), intersect)

    def test_no_intersection(self):
        headA, headB, _ = build_intersecting_lists([], [2, 6, 4], [1, 5])
        self.assertIsNone(self.solution._get_intersection_node(headA, headB))

    def test_intersection_at_last_node(self):
        headA, headB, intersect = build_intersecting_lists([7], [3, 2], [1])
        self.assertIs(self.solution._get_intersection_node(headA, headB), intersect)

    def test_same_list(self):
        common = [1, 2, 3]
        head, _, intersect = build_intersecting_lists(common, [], [])
        self.assertIs(self.solution._get_intersection_node(head, head), intersect)

    def test_empty_lists(self):
        self.assertIsNone(self.solution._get_intersection_node(None, None))


if __name__ == "__main__":
    unittest.main()
