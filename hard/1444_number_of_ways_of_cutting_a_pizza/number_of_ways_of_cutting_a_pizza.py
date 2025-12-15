from functools import lru_cache

class Solution:
    def ways(self, pizza, k):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _count_ways() for actual implementation.
        """
        return self._count_ways(pizza, k)

    def _count_ways(self, pizza, k):
        """
        Internal implementation.  
        Using DP for computing number of valid ways to cut pizza.

        Approach:
            - Use 2D prefix sums to quickly check whether a submatrix contains apples.
            - Define 3D DP:
                dp[remain][r][c]: number of ways to cut sub-pizza (r,c) into `remain` pieces.
            - Base case: remain == 1
                If region has ≥1 apple -> 1, else -> 0
            - Transitions:
                Try horizontal and vertical cuts.
                Only valid if the cut-off region contains ≥1 apple.

        Time Complexity: O(k * m * n * [m + n]) — due to trying horizontal and vertical cuts.  
        Space Complexity: O(k * m * n)

        Args:
            pizza (List[str]): List of strings representing pizza grid (A or .)
            k (int): Number of pieces required.

        Returns:
            int: Number of valid ways modulo 1e9+7.
        """
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # prefix[i][j] = apples in rectangle (i,j) → (m-1,n-1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefix[i][j] = (
                    prefix[i + 1][j] +
                    prefix[i][j + 1] -
                    prefix[i + 1][j + 1] +
                    (1 if pizza[i][j] == 'A' else 0)
                )

        # Check if region (r1,c1) -> (r2,c2) has apple
        def has_apple(r1, c1, r2, c2):
            return (
                prefix[r1][c1]
                - prefix[r2 + 1][c1]
                - prefix[r1][c2 + 1]
                + prefix[r2 + 1][c2 + 1]
            ) > 0

        @lru_cache(None)
        def dp(remain, r, c):
            if prefix[r][c] == 0:
                return 0

            if remain == 1:
                return 1

            ways = 0

            # horizontal cuts
            for nr in range(r + 1, m):
                # top piece = rows [r .. nr-1], columns [c .. n-1]
                if has_apple(r, c, nr - 1, n - 1):
                    ways = (ways + dp(remain - 1, nr, c)) % MOD

            # vertical cuts
            for nc in range(c + 1, n):
                # left piece = rows [r .. m-1], columns [c .. nc-1]
                if has_apple(r, c, m - 1, nc - 1):
                    ways = (ways + dp(remain - 1, r, nc)) % MOD

            return ways

        return dp(k, 0, 0)