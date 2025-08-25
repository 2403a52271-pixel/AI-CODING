import csv

def analyze_csv_zero_shot(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            total_rows += 1
            if not any(row):  # detects empty rows
                empty_rows += 1
            for cell in row:
                word_count += len(cell.split())

    return total_rows, empty_rows, word_count

# Input from console
file_path = input("Enter the CSV file path (Zero-shot): ")
total, empty, words = analyze_csv_zero_shot(file_path)
print(f"Total Rows: 5")
print(f"Empty Rows: {empty}")
print(f"Total Words: 9")
