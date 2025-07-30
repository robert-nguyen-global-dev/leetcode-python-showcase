import pytest
from palindrome_linked_list import Solution, ListNode


@pytest.fixture
def solution():
    return Solution()


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def test_palindrome_even(solution):
    head = build_linked_list([1, 2, 2, 1])
    assert solution._is_palindrome(head) is True

def test_palindrome_odd(solution):
    head = build_linked_list([1, 2, 3, 2, 1])
    assert solution._is_palindrome(head) is True

def test_not_palindrome(solution):
    head = build_linked_list([1, 2])
    assert solution._is_palindrome(head) is False

def test_single_element(solution):
    head = build_linked_list([7])
    assert solution._is_palindrome(head) is True

def test_empty_list(solution):
    head = None
    assert solution._is_palindrome(head) is True
