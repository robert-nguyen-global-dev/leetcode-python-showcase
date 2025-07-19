import unittest
from remove_duplicates_sorted_array import Solution


# 🧪 Unit tests for internal logic `_remove_duplicates`
class TestRemoveDuplicatesSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sorted_array_with_duplicates(self):
        nums = [1, 1, 2]
        expected = [1, 2]
        length = self.solution._remove_duplicates(nums)
        self.assertEqual(length, len(expected))
        self.assertEqual(nums[:length], expected)

    def test_longer_sorted_array_with_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4]
        length = self.solution._remove_duplicates(nums)
        self.assertEqual(length, len(expected))
        self.assertEqual(nums[:length], expected)

    def test_empty_array(self):
        nums = []
        expected = []
        length = self.solution._remove_duplicates(nums)
        self.assertEqual(length, len(expected))
        self.assertEqual(nums[:length], expected)


if __name__ == '__main__':
    unittest.main()
