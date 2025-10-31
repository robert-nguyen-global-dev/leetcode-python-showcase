class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _trap() for actual implementation.
        """
        return self._trap(height)

    def _trap(self, height: list[int]) -> int:
        """
        Internal implementation.  
        Using Two Pointers Technique.

        Idea:
        - Maintain two pointers: left (start) and right (end).
        - Keep track of current max heights from both sides: left_max and right_max.
        - Move the pointer at the side with smaller height inward:
            - If height[left] < height[right]:
                - If height[left] >= left_max → update left_max.
                - Else, accumulate (left_max - height[left]).
                - Move left pointer.
            - Else:
                - If height[right] >= right_max → update right_max.
                - Else, accumulate (right_max - height[right]).
                - Move right pointer.

        Time Complexity: O(n)  
        Space Complexity: O(1)

        Args:
            height (List[int]): Non-negative integers representing elevation map.

        Returns:
            int: Total units of trapped water.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped += right_max - height[right]
                right -= 1

        return trapped
