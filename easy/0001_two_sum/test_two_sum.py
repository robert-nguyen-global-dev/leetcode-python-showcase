import unittest 
from two_sum import Solution


# Internal logic test only
class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution._two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        self.assertEqual(self.solution._two_sum([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(self.solution._two_sum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()