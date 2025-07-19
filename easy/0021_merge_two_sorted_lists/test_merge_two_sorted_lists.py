import unittest
from merge_two_sorted_lists import ListNode, Solution


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    
    for value in values:
        current.next = ListNode(value)
        current = current.next
        
    return dummy.next


# Internal logic test only
class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        list1 = build_linked_list([1, 2, 4])
        list2 = build_linked_list([1, 3, 4])
        expected_result = build_linked_list([1, 1, 2, 3, 4, 4])
        self.assertEqual(self.solution._merge_two_lists(list1, list2), expected_result)

    def test_case_2(self):
        list1 = build_linked_list([])
        list2 = build_linked_list([])
        expected_result = build_linked_list([])
        self.assertEqual(self.solution._merge_two_lists(list1, list2), expected_result)

    def test_case_3(self):
        list1 = build_linked_list([])
        list2 = build_linked_list([0])
        expected_result = build_linked_list([0])
        self.assertEqual(self.solution._merge_two_lists(list1, list2), expected_result)


if __name__ == '__main__':
    unittest.main()
