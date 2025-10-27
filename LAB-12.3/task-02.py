def bubble_sort(lst):
    """
    Performs bubble sort on lst in-place.
    Returns the sorted list.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap elements
    return lst

# Example usage
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_list)
    sorted_list = bubble_sort(test_list.copy())
    print("Sorted list:", sorted_list)

    # Verify if the list is actually sorted
    is_sorted = all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1))
    print("Is the list sorted?", "Yes" if is_sorted else "No")
