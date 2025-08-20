from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_find_relative_ranks()` for actual implementation.
        """
        return self._find_relative_ranks(score)

    def _find_relative_ranks(self, score: List[int]) -> List[str]:
        """
        Internal implementation.  
        Assigns relative ranks to athletes based on their scores.

        Approach:
        - Pair each score with its original index.
        - Sort the list in descending order of scores.
        - Assign medals for the top 3 athletes.
        - Assign numeric ranks for the remaining athletes.
        - Place results back in the correct original order.

        Time Complexity: O(n log n) — due to sorting.  
        Space Complexity: O(n) — for storing ranks.

        Args:
            score (List[int]): List of athletes' scores.

        Returns:
            List[str]: Relative ranks or medals for each athlete.
        """
        n = len(score)
        result = [""] * n

        # Pair score with original index and sort by score descending
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        for rank, (index, _) in enumerate(sorted_scores, start=1):
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)

        return result
