def count_lines_in_file(file_path):
    """
    Reads a file and returns the number of lines.
    Parameters:
    file_path (str): Path to the file.
    Returns:
    int: Number of lines in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
file_path = 'Task2.py'
line_count = count_lines_in_file(file_path)
print(f"The file has {line_count} lines.")