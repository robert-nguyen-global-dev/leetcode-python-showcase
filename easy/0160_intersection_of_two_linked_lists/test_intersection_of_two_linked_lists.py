import pytest
from intersection_of_two_linked_lists import ListNode, Solution


def build_intersecting_lists(common: list[int], listA: list[int], listB: list[int]) -> tuple[ListNode, ListNode, ListNode]:
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


@pytest.fixture
def solution():
    return Solution()


def test_intersection_exists(solution):
    headA, headB, intersect = build_intersecting_lists([8, 4, 5], [4, 1], [5, 6, 1])
    assert solution._get_intersection_node(headA, headB) is intersect

def test_no_intersection(solution):
    headA, headB, _ = build_intersecting_lists([], [2, 6, 4], [1, 5])
    assert solution._get_intersection_node(headA, headB) is None

def test_intersection_at_last_node(solution):
    headA, headB, intersect = build_intersecting_lists([7], [3, 2], [1])
    assert solution._get_intersection_node(headA, headB) is intersect

def test_same_list(solution):
    common = [1, 2, 3]
    head, _, intersect = build_intersecting_lists(common, [], [])
    assert solution._get_intersection_node(head, head) is intersect

def test_empty_lists(solution):
    assert solution._get_intersection_node(None, None) is None
