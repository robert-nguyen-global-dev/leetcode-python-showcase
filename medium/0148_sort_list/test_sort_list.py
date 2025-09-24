import pytest
from sort_list import Solution, ListNode


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    head = build_linked_list([4, 2, 1, 3])
    sorted_head = solution._sort_list(head)
    assert linked_list_to_list(sorted_head) == [1, 2, 3, 4]


def test_case_2(solution):
    head = build_linked_list([-1, 5, 3, 4, 0])
    sorted_head = solution._sort_list(head)
    assert linked_list_to_list(sorted_head) == [-1, 0, 3, 4, 5]


def test_case_empty(solution):
    assert solution._sort_list(None) is None


def test_case_single(solution):
    head = build_linked_list([1])
    sorted_head = solution._sort_list(head)
    assert linked_list_to_list(sorted_head) == [1]
