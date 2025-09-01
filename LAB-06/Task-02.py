def print_multiples_for(num):
    print(f"First 10 multiples of {num} using for loop:")
    for i in range(1, 11):
        print(num * i, end=' ')
    print()
def print_multiples_while(num):
    print(f"First 10 multiples of {num} using while loop:")
    i = 1
    while i <= 10:
        print(num * i, end=' ')
        i += 1
    print()
number = 5
print_multiples_for(number)
print_multiples_while(number)
