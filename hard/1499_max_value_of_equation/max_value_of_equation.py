class Solution:
    def findMaxValueOfEquation(self, points, k):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_max_value_of_equation() for actual implementation.
        """
        return self._find_max_value_of_equation(points, k)

    def _find_max_value_of_equation(self, points, k):
        """
        Internal implementation.  
        Uses a monotonic deque to maintain candidates maximizing (y_i - x_i).

        Time Complexity: O(n)  
        Space Complexity: O(n)

        Args:
            points (List[List[int]]): List of [x, y] points sorted by x.
            k (int): Maximum allowed difference in x-values.

        Returns:
            int: Maximum equation value.
        """
        from collections import deque

        dq = deque()  # stores pairs (value = y_i - x_i, x_i)
        best = float('-inf')

        for xj, yj in points:
            # Remove points with x difference > k
            while dq and xj - dq[0][1] > k:
                dq.popleft()

            # Evaluate best candidate
            if dq:
                best = max(best, dq[0][0] + xj + yj)

            # Compute current transformed value
            curr = yj - xj

            # Maintain deque decreasing by 'value'
            while dq and dq[-1][0] <= curr:
                dq.pop()

            dq.append((curr, xj))

        return best
