import pytest
from linked_list_cycle import Solution, ListNode


def create_linked_list(values, pos):
    """
    Helper to create linked list with optional cycle.

    Args:
        values (list): List of node values.
        pos (int): Index to connect tail to (-1 for no cycle).

    Returns:
        ListNode: Head of the linked list.
    """
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


@pytest.fixture
def solution():
    return Solution()


def test_cycle_exists(solution):
    head = create_linked_list([3, 2, 0, -4], 1)
    assert solution._has_cycle(head)

def test_no_cycle(solution):
    head = create_linked_list([1, 2], -1)
    assert not solution._has_cycle(head)

def test_single_node_no_cycle(solution):
    head = create_linked_list([1], -1)
    assert not solution._has_cycle(head)

def test_single_node_with_cycle(solution):
    head = create_linked_list([1], 0)
    assert solution._has_cycle(head)

def test_long_list_with_cycle(solution):
    head = create_linked_list(list(range(1000)), 500)
    assert solution._has_cycle(head)

def test_long_list_without_cycle(solution):
    head = create_linked_list(list(range(1000)), -1)
    assert not solution._has_cycle(head)
