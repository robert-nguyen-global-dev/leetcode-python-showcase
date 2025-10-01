import pytest
from linked_list_cycle_ii import Solution, ListNode


def build_cycle_list(values, pos):
    """
    Build linked list with a cycle.  
    pos = index of node where tail connects, -1 = no cycle.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(values)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    head = build_cycle_list([3,2,0,-4], pos=1)
    cycle_node = solution._detectCycle(head)
    assert cycle_node.val == 2

def test_case_2(solution):
    head = build_cycle_list([1,2], pos=0)
    cycle_node = solution._detectCycle(head)
    assert cycle_node.val == 1

def test_case_3(solution):
    head = build_cycle_list([1], pos=-1)
    cycle_node = solution._detectCycle(head)
    assert cycle_node is None
