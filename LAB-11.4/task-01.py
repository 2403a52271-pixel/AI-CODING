class Stack:
    """A simple implementation of a stack (LIFO) data structure.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item from the stack. Raises IndexError if empty.
        peek(): Return the top item without removing it. Raises IndexError if empty.
        is_empty(): Return True if the stack is empty, False otherwise.
    """

    def __init__(self):
        """Initialize the stack using a list."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack.

        Args:
            item: The element to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

# Test stack operations using sample data
if __name__ == "__main__":
    stack = Stack()
    print("Pushing items: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack peek:", stack.peek())    # Should print 3
    print("Stack pop:", stack.pop())      # Should print 3
    print("Stack peek after pop:", stack.peek())  # Should print 2
    print("Is stack empty?", stack.is_empty())    # Should print False
    stack.pop()
    stack.pop()
    print("Is stack empty after popping all elements?", stack.is_empty())  # Should print True
    try:
        stack.pop()
    except IndexError as e:
        print("Error when popping from empty stack:", e)

# Optimization/Alternative Suggestion:
# For production use cases requiring fast appends and pops from both ends (not just LIFO/stack),
# consider using collections.deque instead of list. deque provides O(1) time complexity
# for append/pop operations, whereas list's pop(0) is O(n).
# For classic stack (LIFO) operations, Python's built-in list is sufficient and efficient.
