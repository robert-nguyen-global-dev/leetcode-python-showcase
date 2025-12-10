class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _orderly_queue() for actual implementation.
        """
        return self._orderly_queue(s, k)

    def _orderly_queue(self, s: str, k: int) -> str:
        """
        Internal implementation.

        Case 1: k == 1 → return min rotation of s
        Case 2: k >= 2 → return sorted(s)

        Time Complexity: O(n²)  
        Space Complexity: O(N * 2^N)

        Args:
            s (str): input string
            k (int): allowed moves

        Returns:
            str: lexicographically smallest possible string
        """
        if k == 1:
            # generate all rotations and pick the smallest
            best = s
            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                if rotated < best:
                    best = rotated
            return best

        # If k >= 2 → any permutation is possible → sort string
        return ''.join(sorted(s))
