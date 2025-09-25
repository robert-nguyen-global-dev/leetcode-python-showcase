class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _search_matrix() for actual implementation.
        """
        return self._search_matrix(matrix, target)

    def _search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Internal implementation.  
        Uses binary search on flattened index space.

        Time Complexity: O(log(m*n))  
        Space Complexity: O(1)

        Args:
            matrix (list[list[int]]): 2D matrix with m rows, n columns.
            target (int): Number to search.

        Returns:
            bool: True if target exists in matrix, False otherwise.
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
