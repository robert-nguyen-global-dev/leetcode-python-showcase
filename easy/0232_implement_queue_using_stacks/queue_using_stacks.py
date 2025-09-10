class MyQueue:
    def __init__(self):
        """
        Initialize two stacks.  
        stack_in  -> used for push operations  
        stack_out -> used for pop/peek operations
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.  
        Time Complexity: O(1)
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue.  
        Time Complexity: Amortized O(1)
        """
        self._shift_stacks()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.  
        Time Complexity: Amortized O(1)
        """
        self._shift_stacks()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.  
        Time Complexity: O(1)
        """
        return not self.stack_in and not self.stack_out

    def _shift_stacks(self) -> None:
        """
        Move elements from stack_in to stack_out if needed.  
        This happens only when stack_out is empty.  
        Space Complexity: O(n)
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
