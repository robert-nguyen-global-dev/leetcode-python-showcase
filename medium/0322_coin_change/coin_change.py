class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _coin_change() for actual implementation.
        """
        return self._coin_change(coins, amount)

    def _coin_change(self, coins: list[int], amount: int) -> int:
        """
        Internal implementation.  
        Uses bottom-up dynamic programming approach.

        Time Complexity: O(amount × n) where n = len(coins)  
        Space Complexity: O(amount)

        Args:
            coins (List[int]): List of available coin denominations.
            amount (int): Target amount to make up.

        Returns:
            int: Minimum number of coins needed to make up the amount, or -1 if impossible.
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
