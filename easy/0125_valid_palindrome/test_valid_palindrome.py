import unittest
from valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))

    def test_only_symbols(self):
        self.assertTrue(self.solution.isPalindrome("!!@@##$$"))

    def test_numeric_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("12321"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("Noon"))


if __name__ == "__main__":
    unittest.main()
