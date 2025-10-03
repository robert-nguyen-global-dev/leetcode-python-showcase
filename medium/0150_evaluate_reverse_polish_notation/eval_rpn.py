from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _evalRPN() for actual implementation.
        """
        return self._evalRPN(tokens)

    def _evalRPN(self, tokens: List[str]) -> int:
        """
        Internal implementation.  
        Using stack-based evaluation.

        Time Complexity: O(n) — each token processed once.  
        Space Complexity: O(n) — stack for storing numbers.

        Args:
            tokens (List[str]): List of tokens in Reverse Polish Notation.

        Returns:
            int: Result of evaluating the RPN expression.
        """
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # truncate toward zero
                    stack.append(int(a / b))
        return stack[-1]
