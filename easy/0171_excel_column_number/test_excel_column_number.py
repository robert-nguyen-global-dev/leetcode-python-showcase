import unittest
from excel_column_number import Solution


# 🧪 Unit tests for internal logic `_title_to_number()`
class TestExcelColumnNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_letter(self):
        self.assertEqual(self.solution._title_to_number("A"), 1)
        self.assertEqual(self.solution._title_to_number("Z"), 26)

    def test_double_letter(self):
        self.assertEqual(self.solution._title_to_number("AA"), 27)
        self.assertEqual(self.solution._title_to_number("AZ"), 52)
        self.assertEqual(self.solution._title_to_number("ZZ"), 702)

    def test_triple_letter(self):
        self.assertEqual(self.solution._title_to_number("AAA"), 703)
        self.assertEqual(self.solution._title_to_number("ABC"), 731)

    def test_large_column(self):
        self.assertEqual(self.solution._title_to_number("FXSHRXW"), 2147483647)  # Max 32-bit int


if __name__ == "__main__":
    unittest.main()
