def linear_search(lst, value):
    """
    Performs a linear search for value in lst.
    Returns the index of the value if found, else returns -1.
    """
    for i, item in enumerate(lst):
        if item == value:
            return i
    return -1

# Example usage:
if __name__ == "__main__":
    my_list = [4, 2, 7, 1, 9, 3]
    search_value = 9
    index = linear_search(my_list, search_value)
    if index != -1:
        print(f"Value {search_value} found at index {index}")
    else:
        print(f"Value {search_value} not found in the list")

