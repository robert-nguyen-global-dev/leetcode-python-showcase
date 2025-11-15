class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _count_vowel_permutation() for the full implementation.
        """
        return self._count_vowel_permutation(n)

    def _count_vowel_permutation(self, n: int) -> int:
        """
        Internal implementaton.  
        Dynamic Programming approach using rolling variables.

        Each vowel can follow only specific vowels (reverse transitions):
            a -> e, i, u
            e -> a, i
            i -> a, e, o, u
            o -> i, u
            u -> a, i

        We maintain counts of strings ending in each vowel at each length.

        Time Complexity: O(n)  
        Space Complexity: O(1) — constant space DP.

        Args:
            n (int): Length of the vowel string.

        Returns:
            int: Number of valid vowel permutations modulo 1e9+7.
        """
        MOD = 10**9 + 7

        if n <= 0:
            return 0

        # Initial counts for strings of length 1
        a = e = i = o = u = 1

        for _ in range(2, n + 1):
            na = (e + i + u) % MOD      # a <- e, i, u
            ne = (a + i) % MOD          # e <- a, i
            ni = (e + o) % MOD          # i <- e, o
            no = i % MOD                # o <- i
            nu = (i + o) % MOD          # u <- i, o

            a, e, i, o, u = na, ne, ni, no, nu

        return (a + e + i + o + u) % MOD
