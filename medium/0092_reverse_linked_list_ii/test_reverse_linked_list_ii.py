import pytest
from reverse_linked_list_ii import Solution, ListNode


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


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
    head = build_linked_list([1, 2, 3, 4, 5])
    left, right = 2, 4
    result = solution._reverse_between(head, left, right)
    assert linked_list_to_list(result) == [1, 4, 3, 2, 5]


def test_case_2(solution):
    head = build_linked_list([5])
    result = solution._reverse_between(head, 1, 1)
    assert linked_list_to_list(result) == [5]


def test_case_3(solution):
    head = build_linked_list([1, 2, 3])
    result = solution._reverse_between(head, 1, 2)
    assert linked_list_to_list(result) == [2, 1, 3]
