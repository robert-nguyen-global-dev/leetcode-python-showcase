import unittest
from single_number import Solution


# 🧪 Unit tests for internal logic `_single_number()`
class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution._single_number([2, 2, 1]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution._single_number([4, 1, 2, 1, 2]), 4)

    def test_single_element(self):
        self.assertEqual(self.solution._single_number([99]), 99)

    def test_large_numbers(self):
        self.assertEqual(self.solution._single_number([10**9, 10**9, 42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(self.solution._single_number([-1, -1, -2]), -2)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.solution._single_number([-1, 2, 2, -1, 3]), 3)


if __name__ == "__main__":
    unittest.main()
