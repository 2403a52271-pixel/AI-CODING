def factorial(n: int):
    if n < 0:
        return "Invalid input: factorial not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Taking input from the user
num = int(input("Enter a number: "))
print(f"Factorial of {num} is:", factorial(num))