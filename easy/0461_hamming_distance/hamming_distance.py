class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_hamming_distance()` for actual implementation.
        """
        return self._hamming_distance(x, y)

    def _hamming_distance(self, x: int, y: int) -> int:
        """
        Internal implementation.  
        Computes the Hamming distance between two integers x and y.

        Approach:
        - Use XOR (^) to find differing bits.
        - Count the number of set bits (1s) in the XOR result.

        Time Complexity: O(1) — maximum 32 iterations for a 32-bit integer.  
        Space Complexity: O(1) — constant extra space.

        Args:
            x (int): First integer.
            y (int): Second integer.

        Returns:
            int: The Hamming distance between x and y.
        """
        xor = x ^ y
        distance = 0
        while xor:
            xor &= xor - 1  # remove the lowest set bit
            distance += 1
        return distance