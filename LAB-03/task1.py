def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    raw = input("Enter number(s) (separate by space or comma): ").strip()
    if not raw:
        print("No input provided.")
    else:
        tokens = raw.replace(',', ' ').split()
        for token in tokens:
            try:
                n = int(token)
                if n < 0:
                    print(f"Factorial is not defined for negative number: {n}")
                else:
                    print(f"{n}! = {factorial(n)}")
            except ValueError:
                print(f"Invalid integer: {token}")

