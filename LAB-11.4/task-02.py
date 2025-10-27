
# Implementation 1: Queue using Python list
class QueueList:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self._items) == 0

# Test QueueList
if __name__ == "__main__":
    print("Testing QueueList (using Python list):")
    queue1 = QueueList()
    queue1.enqueue(10)
    queue1.enqueue(20)
    queue1.enqueue(30)
    print("Dequeued:", queue1.dequeue()) # Should print 10
    print("Queue empty?", queue1.is_empty())
    print("Dequeued:", queue1.dequeue()) # Should print 20
    print("Dequeued:", queue1.dequeue()) # Should print 30
    print("Queue empty after all dequeues?", queue1.is_empty())
    try:
        queue1.dequeue()
    except IndexError as e:
        print("Dequeue from empty queue raises error:", e)

print("\n---\n")

# AI Performance Review and Alternative Suggestion:
# -------------------------------------------------
# When using list.pop(0) to dequeue, all subsequent elements must be shifted left,
# making each dequeue operation O(n) time complexity (where n is number of elements).
# For many queue operations (e.g., in a loop), this can be a significant performance bottleneck.
# To achieve O(1) enqueue and dequeue (from both ends), Python's collections.deque is ideal.

from collections import deque

# Implementation 2: Queue using collections.deque (optimized)
class QueueDeque:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self._items) == 0

# Test QueueDeque (optimized version)
if __name__ == "__main__":
    print("Testing QueueDeque (using collections.deque):")
    queue2 = QueueDeque()
    queue2.enqueue(100)
    queue2.enqueue(200)
    queue2.enqueue(300)
    print("Dequeued:", queue2.dequeue())  # Should print 100
    print("Queue empty?", queue2.is_empty())
    print("Dequeued:", queue2.dequeue())  # Should print 200
    print("Dequeued:", queue2.dequeue())  # Should print 300
    print("Queue empty after all dequeues?", queue2.is_empty())
    try:
        queue2.dequeue()
    except IndexError as e:
        print("Dequeue from empty queue raises error:", e)
print("\n")
print("Performance Comparison AI-Generated Summary:")
print("""
- Using a Python list for a queue (with enqueue as append and dequeue as pop(0)) is simple,
  but has poor performance when the queue grows large because pop(0) is O(n).
- Using collections.deque, both enqueue and dequeue operations are O(1).
  This makes deque the preferred choice for efficient, real-world queue implementations in Python.
""")