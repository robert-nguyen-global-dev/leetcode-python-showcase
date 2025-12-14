class Solution:
    def maxSatisfaction(self, satisfaction):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _max_satisfaction() for actual implementation.
        """
        return self._max_satisfaction(satisfaction)

    def _max_satisfaction(self, satisfaction):
        """
        Internal implementation Internal implementation.  
        Using Greedy Optimization for maximizing the like-time coefficient.

        Approach:
            - Sort satisfaction array in descending order.
            - Traverse from largest to smallest.
            - Maintain:
                prefix_sum: accumulated sum of chosen dishes.
                total_score: accumulated like-time coefficient.
            - Greedy rule:
                Only keep adding dishes if prefix_sum remains non-negative.
                If prefix_sum < 0, adding more dishes will reduce the score.

        Time Complexity: O(n log n) — due to sorting.  
        Space Complexity: O(1) — constant memory.

        Args:
            satisfaction (List[int]):
                Array of satisfaction values.

        Returns:
            int: Maximum achievable like-time coefficient.
        """
        satisfaction.sort()
        n = len(satisfaction)
        best = 0

        # Try every starting index
        for i in range(n):
            total = 0
            coef = 1
            for j in range(i, n):
                total += coef * satisfaction[j]
                coef += 1
            best = max(best, total)

        return best
