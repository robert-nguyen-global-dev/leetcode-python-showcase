class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _coin_change_ways() for actual implementation.
        """
        return self._coin_change_ways(amount, coins)

    def _coin_change_ways(self, amount: int, coins: list[int]) -> int:
        """
        Internal implementation.  
        Uses bottom-up dynamic programming to count combinations.

        Time Complexity: O(amount × n) where n = len(coins)  
        Space Complexity: O(amount)

        Args:
            amount (int): Target amount.
            coins (List[int]): List of coin denominations.

        Returns:
            int: Number of combinations to make up the amount.
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
