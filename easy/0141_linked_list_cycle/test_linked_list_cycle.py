import unittest
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


# 🧪 Unit tests for internal logic `_has_cycle()`
class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cycle_exists(self):
        head = create_linked_list([3, 2, 0, -4], 1)
        self.assertTrue(self.solution._has_cycle(head))

    def test_no_cycle(self):
        head = create_linked_list([1, 2], -1)
        self.assertFalse(self.solution._has_cycle(head))

    def test_single_node_no_cycle(self):
        head = create_linked_list([1], -1)
        self.assertFalse(self.solution._has_cycle(head))

    def test_single_node_with_cycle(self):
        head = create_linked_list([1], 0)
        self.assertTrue(self.solution._has_cycle(head))

    def test_long_list_with_cycle(self):
        head = create_linked_list(list(range(1000)), 500)
        self.assertTrue(self.solution._has_cycle(head))

    def test_long_list_without_cycle(self):
        head = create_linked_list(list(range(1000)), -1)
        self.assertFalse(self.solution._has_cycle(head))


if __name__ == "__main__":
    unittest.main()
