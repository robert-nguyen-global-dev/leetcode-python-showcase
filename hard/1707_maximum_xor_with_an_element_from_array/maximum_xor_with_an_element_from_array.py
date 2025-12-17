from typing import List, Tuple


class _BitTrieNode:
    __slots__ = ("child",)

    def __init__(self):
        # child[0] -> bit 0 branch, child[1] -> bit 1 branch
        self.child = [None, None]


class _BitTrie:
    """
    Binary Trie for non-negative integers (supports up to 31 bits for typical 32-bit ints).
    Provides insert(value) and max_xor(value) -> best xor result with some inserted number.
    """
    def __init__(self):
        self.root = _BitTrieNode()
        self.MAX_BIT = 30  # enough for values <= 10^9 (2^30 ~ 1e9)

    def insert(self, num: int) -> None:
        node = self.root
        for b in range(self.MAX_BIT, -1, -1):
            bit = (num >> b) & 1
            if node.child[bit] is None:
                node.child[bit] = _BitTrieNode()
            node = node.child[bit]

    def max_xor(self, num: int) -> int:
        """
        Return maximum (num XOR x) among x inserted in trie.
        Assumes trie is non-empty.
        """
        node = self.root
        xor_val = 0
        for b in range(self.MAX_BIT, -1, -1):
            bit = (num >> b) & 1
            # prefer opposite bit to maximize xor
            want = 1 - bit
            if node.child[want] is not None:
                xor_val |= (1 << b)
                node = node.child[want]
            else:
                node = node.child[bit]
        return xor_val


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _maximize_xor() for actual implementation.
        """
        return self._maximize_xor(nums, queries)

    def _maximize_xor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Internal implementation.  
        Using:  
            - Sort nums ascending.  
            - Sort queries by m ascending (keep original indices).  
            - Insert nums <= m progressively into a binary trie.  
            - For each query, if trie non-empty compute max xor, else -1.  

        Time Complexity: O([N + Q] * B + N log N + Q log Q) where B ~ 31 (bits), N = len(nums), Q = len(queries)  
        Space Complexity: O(N * B) for trie nodes in worst case.

        Args:
            nums (List[int]): list of integers.
            queries (List[List[int]]): list of [x, m] queries.

        Returns:
            List[int]: list of answers in original queries order.
        """
        # Sort nums
        nums.sort()
        # Attach original indices to queries and sort by m
        enumerated_queries: List[Tuple[int, int, int]] = [
            (m, x, i) for i, (x, m) in enumerate(queries)
        ]
        enumerated_queries.sort(key=lambda t: t[0])

        trie = _BitTrie()
        res = [-1] * len(queries)
        ni = 0
        n = len(nums)

        for m, x, qi in enumerated_queries:
            # Insert eligible nums <= m
            while ni < n and nums[ni] <= m:
                trie.insert(nums[ni])
                ni += 1

            # If trie empty (no nums <= m), answer is -1
            if trie.root.child[0] is None and trie.root.child[1] is None:
                res[qi] = -1
            else:
                res[qi] = trie.max_xor(x)

        return res
