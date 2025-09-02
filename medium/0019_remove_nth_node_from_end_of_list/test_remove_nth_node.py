import pytest
from remove_nth_node import Solution, ListNode


def list_to_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
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


def test_middle_node_removal(solution):
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution._remove_nth_from_end(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]

def test_remove_last_node(solution):
    head = list_to_linked_list([1, 2, 3])
    result = solution._remove_nth_from_end(head, 1)
    assert linked_list_to_list(result) == [1, 2]

def test_remove_head_node(solution):
    head = list_to_linked_list([1, 2, 3])
    result = solution._remove_nth_from_end(head, 3)
    assert linked_list_to_list(result) == [2, 3]

def test_single_node_list(solution):
    head = list_to_linked_list([1])
    result = solution._remove_nth_from_end(head, 1)
    assert linked_list_to_list(result) == []

def test_two_node_list(solution):
    head = list_to_linked_list([1, 2])
    result = solution._remove_nth_from_end(head, 1)
    assert linked_list_to_list(result) == [1]
