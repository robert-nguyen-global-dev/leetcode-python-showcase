from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_all_concatenated_words () for actual implementation.
        """
        return self._find_all_concatenated_words(words)

    def _find_all_concatenated_words(self, words: List[str]) -> List[str]:
        """
        Internal implementation.

        Steps:
        1. Sort words by length (ASC) to ensure smaller building blocks exist first.
        2. Maintain a word_set for O(1) lookups.
        3. Use DFS + memo to check if a word can be formed by at least
           two smaller words.
        
        Time Complexity: O(n * L^2)  
        Space Complexity: O(n * L)

        Args:
            words (List[str]): List of candidate words.

        Returns:
            List[str]: All concatenated words.
        """
        words_sorted = sorted(words, key=len)
        word_set = set()
        memo = {}

        def can_form(word: str, is_original=True) -> bool:
            """
            Check if a word can be formed by concatenating at least two
            shorter words already in word_set.

            Uses DFS + memoization.
            """
            if word in memo and not is_original:
                return memo[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in word_set:
                    # IMPORTANT FIX:
                    # Only allow checking can_form(suffix) if suffix != original word
                    if suffix in word_set or (suffix != word and can_form(suffix, False)):
                        memo[word] = True
                        return True

            memo[word] = False
            return False

        result = []
        for w in words_sorted:
            if not w:
                continue

            if can_form(w):
                result.append(w)

            word_set.add(w)

        return result