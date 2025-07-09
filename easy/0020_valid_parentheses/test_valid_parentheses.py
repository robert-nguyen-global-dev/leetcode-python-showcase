import unittest
from valid_parentheses import Solution

# Internal logic test only
class TestValidParentheses(unittest.TestCase):
    def test_valid_cases(self):
        self.assertTrue(Solution()._is_valid("()"))
        self.assertTrue(Solution()._is_valid("()[]{}"))
        self.assertTrue(Solution()._is_valid("{[()]}"))

    def test_invalid_cases(self):
        self.assertFalse(Solution()._is_valid("(]"))
        self.assertFalse(Solution()._is_valid("([)]"))
        self.assertFalse(Solution()._is_valid("("))
        self.assertFalse(Solution()._is_valid("]"))

    def test_empty_string(self):
        self.assertTrue(Solution()._is_valid(""))

if __name__ == '__main__':
    unittest.main()
