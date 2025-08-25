def factorial(n):
    if n < 0:
        return "Invalid input: factorial not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
print(factorial(3))  # Output: 6
print(factorial(0))  # Output: 1
print(factorial(-2)) # Output: Invalid input: factorial not defined for negative numbers
