class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to `_read_binary_watch()` for actual implementation.
        """
        return self._read_binary_watch(turnedOn)

    def _read_binary_watch(self, turnedOn: int) -> list[str]:
        """
        Internal implementation.  
        Returns all possible times on a binary watch given a number of LEDs that are on.

        This method brute-forces all possible hours (0-11) and minutes (0-59),
        counting the number of LEDs lit (bits set to 1) for each combination.

        Time Complexity: O(720) — since there are 12 hours x 60 minutes to check.  
        Space Complexity: O(1) — output list storage is not counted as extra space.

        Args:
            turnedOn (int): The number of LEDs that are lit.

        Returns:
            list[str]: A list of valid time strings in the format "H:MM".
        """
        result = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result
