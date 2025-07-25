import pytest
from merge_two_sorted_lists import ListNode, Solution


@pytest.fixture
def solution():
    return Solution()

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_case_1(solution):
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    result = solution._merge_two_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

def test_case_2(solution):
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    result = solution._merge_two_lists(list1, list2)
    assert linked_list_to_list(result) == []

def test_case_3(solution):
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    result = solution._merge_two_lists(list1, list2)
    assert linked_list_to_list(result) == [0]
