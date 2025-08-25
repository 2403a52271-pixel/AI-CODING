import csv

def analyze_csv_few_shot(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            total_rows += 1
            if not any(cell.strip() for cell in row):
                empty_rows += 1
            word_count += sum(len(cell.split()) for cell in row)

    return total_rows, empty_rows, word_count

# Input from console
file_path = input("Enter the CSV file path (Few-shot): ")
total, empty, words = analyze_csv_few_shot(file_path)
print(f"Total Rows: {total}")
print(f"Empty Rows: {empty}")
print(f"Total Words: {words}")




