from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _outer_trees() for actual implementation.
        """
        return self._outer_trees(trees)

    def _outer_trees(self, trees: List[List[int]]) -> List[List[int]]:
        """
        Internal implementation.  
        Using the monotonic chain convex hull algorithm.  
        Keeps all boundary collinear points per problem requirement.

        Steps:
        1. Sort all points lexicographically.
        2. Build lower hull using cross-product check.
        3. Build upper hull similarly.
        4. Concatenate and remove duplicates.

        Time Complexity: O(n log n)  
        Space Complexity: O(n)

        Args:
            trees (List[List[int]]): Input points on the 2D plane.

        Returns:
            List[List[int]]: Points forming the fence boundary.
        """
        points = sorted(trees)
        if len(points) <= 1:
            return points

        def cross(o: List[int], a: List[int], b: List[int]) -> int:
            """
            2D cross product of OA × OB.
            Positive: counter-clockwise turn
            Negative: clockwise turn
            Zero: collinear
            """
            return (a[0] - o[0]) * (b[1] - o[1]) - \
                   (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for p in points:
            # Pop while making a clockwise turn (cross < 0)
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Combine, but remove duplicates because lower[0] and upper[0] repeat
        hull = lower[:-1] + upper[:-1]

        # Use a set to remove duplicates but keep order
        seen = set()
        result = []
        for x, y in hull:
            if (x, y) not in seen:
                result.append([x, y])
                seen.add((x, y))

        return result
