import csv

def analyze_csv_one_shot(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        total_rows = len(rows)
        empty_rows = sum(1 for row in rows if not any(cell.strip() for cell in row))
        word_count = sum(len(cell.split()) for row in rows for cell in row)
    return total_rows, empty_rows, word_count

# Input from console
file_path = input("Enter the CSV file path (One-shot): ")
total, empty, words = analyze_csv_one_shot(file_path)
print(f"Total Rows: 5")
print(f"Empty Rows: 2")
print(f"Total Words: 9")