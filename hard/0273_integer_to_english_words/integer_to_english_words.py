class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _number_to_words()  for actual implementation.
        """
        return self._number_to_words(num)

    def _number_to_words(self, num: int) -> str:
        """
        Internal implementation.  
        Convert a non-negative integer into English words.

        Time Complexity: O(1) — because the number has a fixed max length (32-bit).  
        Space Complexity: O(1).

        Args:
            num (int): A non-negative integer (0 <= num <= 2^31 - 1)

        Returns:
            str: English phrase representation of the number.
        """
        if num == 0:
            return "Zero"

        # Constants for mapping
        BELOW_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen",
        ]

        TENS = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def _three_digit_to_words(n: int) -> str:
            """
            Convert a number 0–999 into English words.
            """
            if n == 0:
                return ""

            if n < 20:
                return BELOW_20[n]

            if n < 100:
                return TENS[n // 10] + (" " + BELOW_20[n % 10] if n % 10 else "")

            # 100–999
            return (
                BELOW_20[n // 100]
                + " Hundred"
                + (" " + _three_digit_to_words(n % 100) if n % 100 else "")
            )

        # Build final result
        words = []
        idx = 0

        while num > 0:
            chunk = num % 1000
            if chunk != 0:
                segment = _three_digit_to_words(chunk)
                if THOUSANDS[idx]:
                    segment += " " + THOUSANDS[idx]
                words.append(segment)
            num //= 1000
            idx += 1

        # Reverse because we processed from lowest group → highest
        return " ".join(reversed(words))
