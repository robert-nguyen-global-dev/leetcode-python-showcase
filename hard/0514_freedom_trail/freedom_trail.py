from typing import List, Dict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_rotate_steps() for actual implementation.
        """
        return self._find_rotate_steps(ring, key)

    def _find_rotate_steps(self, ring: str, key: str) -> int:
        """
        Internal implementation.  
        Compute the minimum number of steps
        required to spell the given key using the ring.

        Steps:
        1. Precompute indices of each character in the ring.
        2. Use DFS + memo (top-down DP) on state (ring_position, key_index).
        3. For each needed character in `key[key_index]`, try all possible
           ring positions containing it.
        4. Distance on circular ring computed using minimal rotation.

        Time Complexity: O(n * m * k)  
            n = len(ring)
            m = len(key)
            k = avg occurrences per character
        Space Complexity: O(n * m)

        Args:
            ring (str): Circular ring of characters.
            key (str): Target string to spell.

        Returns:
            int: Minimum steps including rotation + selection.
        """
        n = len(ring)

        # Precompute all positions for each character
        positions: Dict[str, List[int]] = {}
        for i, ch in enumerate(ring):
            positions.setdefault(ch, []).append(i)

        memo = {}

        def dfs(r: int, k: int) -> int:
            """
            DFS with memoization.
            r: current ring index
            k: index into key
            """
            if k == len(key):
                return 0

            if (r, k) in memo:
                return memo[(r, k)]

            target = key[k]
            best_steps = float("inf")

            # Try all ring positions where target character appears
            for pos in positions[target]:
                # Circular distance
                diff = abs(r - pos)
                rotation_cost = min(diff, n - diff)

                # 1 select step after rotation
                total = rotation_cost + 1 + dfs(pos, k + 1)
                best_steps = min(best_steps, total)

            memo[(r, k)] = best_steps
            return best_steps

        return dfs(0, 0)
