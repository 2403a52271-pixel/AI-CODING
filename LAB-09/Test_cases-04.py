# AI-generated test cases for ShoppingCart class

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

def test_shopping_cart():
    print("Testing ShoppingCart class...")

    cart = ShoppingCart()

    # Test 1: Add single item
    cart.add_item("Apple", 1.5)
    assert cart.total_cost() == 1.5, "Test 1 Failed"
    print("Test 1 Passed: Add single item")

    # Test 2: Add multiple items
    cart.add_item("Banana", 0.75)
    cart.add_item("Milk", 2.0)
    assert cart.total_cost() == 1.5 + 0.75 + 2.0, "Test 2 Failed"
    print("Test 2 Passed: Add multiple items")

    # Test 3: Remove an item
    cart.remove_item("Banana")
    assert cart.total_cost() == 1.5 + 2.0, "Test 3 Failed"
    print("Test 3 Passed: Remove an item")

    # Test 4: Remove non-existent item (should not error)
    cart.remove_item("Orange")
    assert cart.total_cost() == 1.5 + 2.0, "Test 4 Failed"
    print("Test 4 Passed: Remove non-existent item")

    # Test 5: Update price of existing item
    cart.add_item("Apple", 2.0)
    assert cart.total_cost() == 2.0 + 2.0, "Test 5 Failed"
    print("Test 5 Passed: Update price of existing item")

    # Test 6: Remove all items
    cart.remove_item("Apple")
    cart.remove_item("Milk")
    assert cart.total_cost() == 0, "Test 6 Failed"
    print("Test 6 Passed: Remove all items")

    # Test 7: Add item with zero price
    cart.add_item("Water", 0.0)
    assert cart.total_cost() == 0.0, "Test 7 Failed"
    print("Test 7 Passed: Add item with zero price")

    # Test 8: Add item with negative price (should allow, but not realistic)
    cart.add_item("Coupon", -5.0)
    assert cart.total_cost() == -5.0, "Test 8 Failed"
    print("Test 8 Passed: Add item with negative price")

    print("All ShoppingCart tests passed.")

if __name__ == "__main__":
    test_shopping_cart()
