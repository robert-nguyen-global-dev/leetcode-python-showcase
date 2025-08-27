import pytest
from add_two_numbers import Solution, ListNode


def build_linked_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
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


def test_example1(solution):
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = solution._add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]

def test_example2(solution):
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = solution._add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [0]

def test_example3(solution):
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    result = solution._add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

def test_edge_case(solution):
    l1 = build_linked_list([5])
    l2 = build_linked_list([5])
    result = solution._add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [0, 1]
