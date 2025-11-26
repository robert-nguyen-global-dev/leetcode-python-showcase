import pytest
from merge_k_sorted_lists import Solution, ListNode


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for val in values:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def list_to_py(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6]),
    ]
    merged = solution._merge_k_lists(lists)
    assert list_to_py(merged) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_case_2(solution):
    lists = []
    merged = solution._merge_k_lists(lists)
    assert list_to_py(merged) == []

def test_case_3(solution):
    lists = [None]
    merged = solution._merge_k_lists(lists)
    assert list_to_py(merged) == []

def test_case_4(solution):
    lists = [
        build_list([1]),
        build_list([0])
    ]
    merged = solution._merge_k_lists(lists)
    assert list_to_py(merged) == [0, 1]
