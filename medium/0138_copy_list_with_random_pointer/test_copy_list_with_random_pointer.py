import pytest
from copy_list_with_random_pointer import Solution, Node


def build_linked_list_with_random(values, random_indices):
    """
    values: list of node values
    random_indices: list of indices for random pointers (-1 means None)
    """
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, idx in enumerate(random_indices):
        nodes[i].random = nodes[idx] if idx != -1 else None
    return nodes[0] if nodes else None


def linked_list_to_list(head):
    result = []
    visited = {}
    i = 0
    while head:
        if head not in visited:
            visited[head] = i
        result.append((head.val, visited.get(head.random, -1)))
        head = head.next
        i += 1
    return result


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    head = build_linked_list_with_random([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
    copied = solution._copy_random_list(head)
    assert linked_list_to_list(copied) == linked_list_to_list(head)


def test_case_2(solution):
    head = build_linked_list_with_random([1, 2], [1, 1])
    copied = solution._copy_random_list(head)
    assert linked_list_to_list(copied) == linked_list_to_list(head)


def test_case_3(solution):
    head = build_linked_list_with_random([3, 3, 3], [-1, 0, -1])
    copied = solution._copy_random_list(head)
    assert linked_list_to_list(copied) == linked_list_to_list(head)


def test_empty(solution):
    assert solution._copy_random_list(None) is None
