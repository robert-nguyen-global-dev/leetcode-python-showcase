import unittest
from best_time_to_buy_and_sell_stock import Solution


# 🧪 Unit tests for internal logic `_max_profit()`
class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution._max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(self.solution._max_profit([7, 6, 4, 3, 1]), 0)

    def test_single_price(self):
        self.assertEqual(self.solution._max_profit([5]), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution._max_profit([]), 0)

    def test_constant_prices(self):
        self.assertEqual(self.solution._max_profit([3, 3, 3, 3]), 0)

    def test_early_peak(self):
        self.assertEqual(self.solution._max_profit([9, 1, 5, 6, 2]), 5)


if __name__ == '__main__':
    unittest.main()
    