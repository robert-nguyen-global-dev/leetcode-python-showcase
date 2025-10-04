class Solution:
    def calculate(self, s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _calculate() for actual implementation.
        """
        return self._calculate(s)

    def _calculate(self, s: str) -> int:
        """
        Internal implementation.  
        Using stack for operator precedence.

        Time Complexity: O(n) — single pass through string.  
        Space Complexity: O(n) — stack for intermediate results.

        Args:
            s (str): Input expression containing digits and operators (+ - * /).

        Returns:
            int: Result of evaluating the expression.
        """
        stack = []
        num = 0
        prev_op = "+"
        s = s.replace(" ", "")

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack.append(stack.pop() * num)
                elif prev_op == "/":
                    top = stack.pop()
                    stack.append(int(top / num))  # truncate toward zero
                prev_op = ch
                num = 0

        return sum(stack)
