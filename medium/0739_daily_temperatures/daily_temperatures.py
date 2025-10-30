class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _daily_temperatures() for actual implementation.
        """
        return self._daily_temperatures(temperatures)

    def _daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """
        Internal implementation.  
        Using a Monotonic Decreasing Stack.

        Idea:
        - Traverse temperatures from right to left.
        - Maintain a stack of indices where temperatures are in decreasing order.
        - For each temperature[i]:
            - Pop from stack while current temperature >= stack top's temperature.
            - If stack not empty → distance = top_index - i.
            - Push current index i onto stack.

        Time Complexity: O(n)  
        Space Complexity: O(n)

        Args:
            temperatures (List[int]): List of daily temperatures.

        Returns:
            List[int]: Number of days to wait for a warmer temperature.
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i in range(n - 1, -1, -1):
            # Step 1: Remove colder or same days
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # Step 2: Compute distance to next warmer day
            if stack:
                answer[i] = stack[-1] - i

            # Step 3: Push current day
            stack.append(i)

        return answer
