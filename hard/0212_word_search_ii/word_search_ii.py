from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_words() for actual implementation.
        """
        return self._find_words(board, words)

    def _find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Internal implementation.  
        Using Trie + DFS backtracking.

        Idea:
        - Build a Trie from the word list for efficient prefix pruning.
        - Perform DFS from each cell of the board if it matches a Trie prefix.
        - Use backtracking to explore valid paths and mark visited cells.
        - Collect words when reaching Trie nodes that represent full words.

        Time Complexity: O(M * N * 4^L) in the worst case, but much faster due to Trie pruning.  
        Space Complexity: O(K * L) for Trie + recursion stack.

        Args:
            board (List[List[str]]): 2D board of characters.
            words (List[str]): List of words to search for.

        Returns:
            List[str]: All words found on the board.
        """
        # Step 1: Build Trie
        root = self._build_trie(words)
        result = set()
        rows, cols = len(board), len(board[0])

        # Step 2: DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    self._dfs(board, r, c, root, result)

        return list(result)

    def _build_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word
        return root

    def _dfs(self, board: List[List[str]], r: int, c: int, node: TrieNode, result: set):
        char = board[r][c]
        curr = node.children[char]

        # Step 1: Word found
        if curr.word:
            result.add(curr.word)

        # Step 2: Mark visited
        board[r][c] = '#'

        # Step 3: Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(board)
                and 0 <= nc < len(board[0])
                and board[nr][nc] in curr.children
            ):
                self._dfs(board, nr, nc, curr, result)

        # Step 4: Restore character
        board[r][c] = char
