
def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.
    Args:
        numbers (list): A list of integers to process
    Returns:
        tuple: A tuple containing (sum_of_even, sum_of_odd)
               - sum_of_even: Sum of all even numbers in the list
               - sum_of_odd: Sum of all odd numbers in the list
    
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5, 6])
        (12, 9)
    """
    sum_even = 0
    sum_odd = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd
# Test the function
if __name__ == "__main__":
    # Example usage
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_sum, odd_sum = sum_even_odd(test_list)

    print(f"Original list: {test_list}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
    print(f"Total sum: {even_sum + odd_sum}")

