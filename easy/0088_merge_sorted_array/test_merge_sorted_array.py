import unittest
from merge_sorted_array import Solution

# 🧪 Unit tests for internal logic `_merge_sorted_array`
class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.solution._merge_sorted_array(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_case_2(self):
        nums1 = [1]
        nums2 = []
        self.solution._merge_sorted_array(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_case_3(self):
        nums1 = [0]
        nums2 = [1]
        self.solution._merge_sorted_array(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

    def test_case_4(self):
        nums1 = [2, 0]
        nums2 = [1]
        self.solution._merge_sorted_array(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [1, 2])

if __name__ == '__main__':
    unittest.main()
