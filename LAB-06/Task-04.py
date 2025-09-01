def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
print("Sum of first 10 numbers using for loop:", sum_to_n_for(10))
print("Sum of first 10 numbers using while loop:", sum_to_n_while(10))
def sum_to_n_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to_n_recursive(n - 1)
print("Sum of first 10 numbers using recursion:", sum_to_n_recursive(10))
def sum_to_n_builtin(n):
    return sum(range(1, n + 1))
print("Sum of first 10 numbers using built-in sum:", sum_to_n_builtin(10))
