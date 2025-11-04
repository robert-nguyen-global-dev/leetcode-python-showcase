from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _ladder_length() for actual implementation.
        """
        return self._ladder_length(beginWord, endWord, wordList)

    def _ladder_length(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Internal implementation.  
        Using BFS to find the shortest transformation sequence.

        Idea:
        - Treat each word as a node.
        - Two words are connected if they differ by exactly one character.
        - Perform BFS starting from beginWord.
        - Stop when endWord is found — first occurrence guarantees shortest path.

        Time Complexity: O(N * L) where:
            N = number of words, L = length of each word.  
            
        Space Complexity: O(N * L)

        Args:
            beginWord (str): Starting word.
            endWord (str): Target word.
            wordList (List[str]): List of valid dictionary words.

        Returns:
            int: Length of the shortest transformation sequence, or 0 if impossible.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, steps + 1))

        return 0
