import unittest
from climbing_stairs import Solution

# 🧪 Unit tests for internal logic `_climb_stairs`
class TestClimbingStairs(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution()._climb_stairs(1), 1)

    def test_case_2(self):
        self.assertEqual(Solution()._climb_stairs(2), 2)

    def test_case_3(self):
        self.assertEqual(Solution()._climb_stairs(3), 3)

    def test_case_4(self):
        self.assertEqual(Solution()._climb_stairs(4), 5)

    def test_case_5(self):
        self.assertEqual(Solution()._climb_stairs(10), 89)

    def test_case_large(self):
        self.assertEqual(Solution()._climb_stairs(45), 1836311903)

if __name__ == '__main__':
    unittest.main()
