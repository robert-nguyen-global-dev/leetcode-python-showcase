import pytest
from reverse_linked_list import Solution, ListNode


def list_to_linkedlist(items):
    """Helper to convert list to linked list."""
    dummy = ListNode()
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    """Helper to convert linked list back to list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.fixture
def solution():
    return Solution()


def test_reverse_example(solution):
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    reversed_head = solution._reverse_list(head)
    assert linkedlist_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_single_node(solution):
    head = list_to_linkedlist([1])
    reversed_head = solution._reverse_list(head)
    assert linkedlist_to_list(reversed_head) == [1]

def test_reverse_empty_list(solution):
    head = list_to_linkedlist([])
    reversed_head = solution._reverse_list(head)
    assert linkedlist_to_list(reversed_head) == []

def test_reverse_two_nodes(solution):
    head = list_to_linkedlist([1, 2])
    reversed_head = solution._reverse_list(head)
    assert linkedlist_to_list(reversed_head) == [2, 1]

def test_reverse_duplicates(solution):
    head = list_to_linkedlist([1, 2, 2, 1])
    reversed_head = solution._reverse_list(head)
    assert linkedlist_to_list(reversed_head) == [1, 2, 2, 1]
