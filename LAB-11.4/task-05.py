class Graph:
    """
    Graph implementation using an adjacency list.
    Supports BFS (Breadth-First Search) and DFS (Depth-First Search) traversals.
    """
    def __init__(self):
        # adjacency_list is a dictionary where each key is a node and value is a list of neighbor nodes
        self.adjacency_list = {}

    def add_edge(self, src, dest):
        """Add an edge from src to dest. The graph is undirected by default."""
        if src not in self.adjacency_list:
            self.adjacency_list[src] = []
        if dest not in self.adjacency_list:
            self.adjacency_list[dest] = []
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)  # Comment this if directed graph

    def bfs(self, start):
        """
        Perform Breadth-First Search starting from node 'start'.
        Returns the list of nodes in BFS order.
        """
        from collections import deque
        visited = set()                # To keep track of visited nodes
        queue = deque([start])         # Queue for BFS
        order = []                     # List to store traversal order

        while queue:
            node = queue.popleft()     # Pop the front node in the queue
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adjacency_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """
        Perform Depth-First Search recursively starting from 'start'.
        Returns the list of nodes in DFS order.
        """
        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            order.append(node)
            # Visit all unvisited neighbors
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(start)
        return order

    def dfs_iterative(self, start):
        """
        Perform Depth-First Search iteratively using a stack.
        Returns the list of nodes in DFS order.
        """
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()      # Pop the top of the stack (LIFO)
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Push all unvisited neighbors onto the stack
                # (Reversed for consistent order with recursive DFS if needed)
                for neighbor in reversed(self.adjacency_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

# -----------------------------------------------
# Example/test usage:
if __name__ == "__main__":
    g = Graph()
    # Constructing the following undirected graph:
    #   A
    #  / \
    # B   C
    # |   |
    # D---E
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')

    print("Adjacency list:", g.adjacency_list)
    print("BFS (from A):", g.bfs('A'))
    print("DFS Recursive (from A):", g.dfs_recursive('A'))
    print("DFS Iterative (from A):", g.dfs_iterative('A'))

    # Comparison Note:
    # - Recursive DFS uses function recursion and may hit recursion limits on very large/deep graphs.
    # - Iterative DFS uses an explicit stack and is less prone to recursion depth issues.
    # - Both achieve the same traversal, but order may differ depending on neighbor order.
    # - BFS explores neighbors level by level, DFS explores as deep as possible before backtracking.
