class Node:
    """
    Represents a node in the Binary Search Tree.
    Contains the value (data), and left and right child references.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation with insert, search, and inorder traversal.
    """

    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the specified data into the BST.
        """
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            # Duplicates are ignored
            return node
        
        self.root = _insert(self.root, data)

    def search(self, key):
        """
        Searches for a node with the specified key.
        Returns True if found, False otherwise.
        """
        def _search(node, key):
            if node is None:
                return False
            if key == node.data:
                return True
            if key < node.data:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)

    def inorder_traversal(self):
        """
        Returns the inorder traversal (sorted sequence) of the BST as a list.
        """
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)
        _inorder(self.root)
        return result

# Testing the BST implementation
if __name__ == "__main__":
    bst = BST()
    nums = [7, 3, 9, 1, 5, 8, 10]
    for num in nums:
        bst.insert(num)
    print("Inorder Traversal:", bst.inorder_traversal())  # Should print [1, 3, 5, 7, 8, 9, 10]
    print("Search 5:", bst.search(5))   # Should print True
    print("Search 11:", bst.search(11)) # Should print False
