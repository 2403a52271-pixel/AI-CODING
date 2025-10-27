class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the node
        self.next = None  # Pointer to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Head initially points to no node

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, make new_node the head
            self.head = new_node
            # AI comment: Head now points to the newly created node.
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the end of the list
            current.next = new_node    # AI comment: The previous last node's 'next' pointer now points to new_node.

    def delete_value(self, value):
        """Delete the first node containing the specified value."""
        current = self.head
        prev = None

        # Search for the node to delete
        while current:
            if current.data == value:
                if prev is None:
                    # AI comment: Deleting the head node. Head is updated to the next node in the list.
                    self.head = current.next
                else:
                    # AI comment: 'prev.next' skips over 'current' (node to delete),
                    # pointing it directly to 'current.next' (the following node).
                    prev.next = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return a list of node data."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements

# -------------------------------
# AI Suggested Test Cases:
# -------------------------------
if __name__ == "__main__":
    ll = LinkedList()
    print("Initial linked list (should be empty):", ll.traverse())

    # Test 1: Insert at end
    ll.insert_at_end(10)
    print("After inserting 10:", ll.traverse())
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After inserting 20, 30:", ll.traverse())

    # Test 2: Delete head value
    ll.delete_value(10)
    print("After deleting head (10):", ll.traverse())

    # Test 3: Delete middle value
    ll.insert_at_end(40)
    print("Inserted 40:", ll.traverse())
    ll.delete_value(30)
    print("After deleting middle value (30):", ll.traverse())

    # Test 4: Delete tail value
    ll.delete_value(40)
    print("After deleting tail (40):", ll.traverse())

    # Test 5: Attempt to delete value not present
    result = ll.delete_value(99)
    print("Attempting to delete non-existing value (99):", result, ll.traverse())

    # Test 6: Delete only remaining value (20) so list is empty again
    ll.delete_value(20)
    print("After deleting last element (20):", ll.traverse())

    # Test 7: Try to delete from empty list
    result = ll.delete_value(10)
    print("Attempt to delete from empty list:", result, ll.traverse())

