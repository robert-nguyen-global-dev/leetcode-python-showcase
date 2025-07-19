import unittest
from roman_to_int import Solution


# Internal logic test only
class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution._roman_to_int("III"), 3)

    def test_case_2(self):
        self.assertEqual(self.solution._roman_to_int("IV"), 4)

    def test_case_3(self):
        self.assertEqual(self.solution._roman_to_int("IX"), 9)

    def test_case_4(self):
        self.assertEqual(self.solution._roman_to_int("LVIII"), 58)  # L=50, V=5, III=3

    def test_case_5(self):
        self.assertEqual(self.solution._roman_to_int("MCMXCIV"), 1994)  # M=1000, CM=900, XC=90, IV=4


if __name__ == '__main__':
    unittest.main()
