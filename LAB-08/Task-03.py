def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    
    print(f"Addition: {num1} + {num2} = {add_numbers(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract_numbers(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply_numbers(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide_numbers(num1, num2)}")
    
    print(f"Division by zero: {num1} / 0 = {divide_numbers(num1, 0)}")

