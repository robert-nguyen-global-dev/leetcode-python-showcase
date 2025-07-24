import unittest
from majority_element import Solution


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_middle(self):
        self.assertEqual(self.solution._majority_element([3, 2, 3]), 3)

    def test_majority_single(self):
        self.assertEqual(self.solution._majority_element([1]), 1)

    def test_majority_end(self):
        self.assertEqual(self.solution._majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_majority_even_length(self):
        self.assertEqual(self.solution._majority_element([1, 1, 2, 1]), 1)

    def test_large_majority(self):
        self.assertEqual(self.solution._majority_element([5]*100 + [1]*49), 5)


if __name__ == "__main__":
    unittest.main()
