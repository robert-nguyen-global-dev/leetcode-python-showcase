from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_ladders() for actual implementation.
        """
        return self._find_ladders(beginWord, endWord, wordList)

    def _find_ladders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        """
        Internal implementation.  
        Using BFS + Backtracking.

        Idea:
        - Use BFS to find shortest transformation distance from beginWord to all reachable words.
        - Build adjacency (predecessor) graph only along shortest paths.
        - Use backtracking to reconstruct all shortest sequences from endWord → beginWord.

        Time Complexity: O(N * L) — where N = len(wordList), L = len(word)  
        Space Complexity: O(N * L)

        Args:
            beginWord (str): Starting word.
            endWord (str): Target word.
            wordList (List[str]): List of valid words.

        Returns:
            List[List[str]]: All shortest transformation sequences.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # Step 1: BFS — build graph relationships
        graph = defaultdict(list)
        level = {beginWord: 0}
        queue = deque([beginWord])
        found = False

        while queue and not found:
            next_level = {}
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word not in word_set:
                            continue
                        if new_word not in level:
                            next_level[new_word] = level[word] + 1
                            queue.append(new_word)
                        if next_level.get(new_word, 0) == level[word] + 1:
                            graph[new_word].append(word)
                        if new_word == endWord:
                            found = True
            level.update(next_level)

        # Step 2: Backtracking — reconstruct all shortest paths
        result = []

        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for prev in graph[word]:
                backtrack(prev, path + [prev])

        if found:
            backtrack(endWord, [endWord])

        return result
