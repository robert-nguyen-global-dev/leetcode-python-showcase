from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.
		
        Delegates to `_max_profit()` for actual implementation.
        """
        return self._max_profit(prices)

    def _max_profit(self, prices: List[int]) -> int:
        """
        Internal implementation.  
        Finds the maximum profit achievable from a single buy-sell transaction of a stock.

        The function iterates through daily prices to track the minimum price seen so far,
        and computes potential profit by selling at the current price. It ensures the buy 
        always occurs before the sell, optimizing profit in a single pass.

        Time Complexity: O(n) — where n is the number of days (length of prices).  
        Space Complexity: O(1) — uses constant space for tracking min price and max profit.

        Args:
            prices (List[int]): List of stock prices where prices[i] is the price on day i.

        Returns:
            int: Maximum profit from one transaction. Returns 0 if no profit can be made.
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
