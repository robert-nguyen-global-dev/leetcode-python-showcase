from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_profit() for actual implementation.
        """
        return self._max_profit(k, prices)

    def _max_profit(self, k: int, prices: List[int]) -> int:
        """
        Internal implementation.  
        Using DP for Best Time to Buy and Sell Stock IV.

        Two DP arrays are maintained:
        - buy[t]  = maximum profit when holding a stock after t transactions
        - sell[t] = maximum profit when not holding a stock after t transactions

        Special case: when k >= n/2, the problem reduces to unlimited transactions.

        Time Complexity: O(k * n)  
        Space Complexity: O(k)

        Args:
            k (int): Maximum number of allowed transactions.
            prices (List[int]): Stock prices over days.

        Returns:
            int: Maximum achievable profit.
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Special case: unlimited transactions allowed
        if k >= n // 2:
            total_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    total_profit += prices[i] - prices[i - 1]
            return total_profit

        # General case: DP with O(k) memory
        NEG_INF = -10**15
        buy = [NEG_INF] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]
