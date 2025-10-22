class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_profit_cooldown() for actual implementation.
        """
        return self._max_profit_cooldown(prices)

    def _max_profit_cooldown(self, prices: list[int]) -> int:
        """
        Internal implementation.  
        Using dynamic programming (state machine).

        State definitions:
            hold[i] — max profit when holding stock after day i
            sold[i] — max profit when sold on day i
            rest[i] — max profit when resting on day i

        Transitions:
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i-1], sold[i-1])

        Time Complexity: O(n)  
        Space Complexity: O(1) — only last state values are needed.

        Args:
            prices (List[int]): List of stock prices by day.

        Returns:
            int: Maximum profit achievable with 1-day cooldown.
        """
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold, prev_sold, prev_rest = hold, sold, rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
