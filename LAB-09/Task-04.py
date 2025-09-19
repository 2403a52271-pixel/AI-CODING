class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        """Add an item with its price to the cart. If item exists, update price."""
        self.items[name] = price

    def remove_item(self, name):
        """Remove an item from the cart by name."""
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        """Return the total cost of all items in the cart."""
        return sum(self.items.values())

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 1.5)
cart.add_item("Banana", 0.75)
cart.add_item("Milk", 2.0)
print("Total cost after adding items:", cart.total_cost())  # Output: 4.25

cart.remove_item("Banana")
print("Total cost after removing Banana:", cart.total_cost())  # Output: 3.5

cart.add_item("Apple", 2.0)  # Update price of Apple
print("Total cost after updating Apple price:", cart.total_cost())  # Output: 4.0
