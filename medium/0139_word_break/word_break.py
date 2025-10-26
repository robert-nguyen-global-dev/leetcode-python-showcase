class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _word_break() for actual implementation.
        """
        return self._word_break(s, wordDict)

    def _word_break(self, s: str, wordDict: list[str]) -> bool:
        """
        Internal implementation.  
        Uing Dynamic Programming.

        dp[i] = True if s[:i] can be segmented into valid words from wordDict.  
        dp[0] = True (base case for empty string)

        Transition:
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))

        Time Complexity: O(n^2).  
        Space Complexity: O(n)

        Args:
            s (str): Input string.
            wordDict (List[str]): List of valid dictionary words.

        Returns:
            bool: True if s can be segmented, False otherwise.
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
