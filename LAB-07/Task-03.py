def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
    Returns:
        int: The nth Fibonacci number.
    Raises:
        ValueError: If n is negative.
    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# Example usage:
if __name__ == "__main__":
    n = 7
    print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")
