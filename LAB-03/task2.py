# Program: Sort numbers in descending order, then ascending order

def read_numbers():
    raw = input("Enter number(s) (separate by space or comma): ").strip()
    if not raw:
        print("No input provided.")
        return []
    tokens = raw.replace(',', ' ').split()
    numbers = []
    for token in tokens:
        try:
            numbers.append(int(token))
        except ValueError:
            print(f"Invalid integer: {token}")
    return numbers

if __name__ == "__main__":
    nums = read_numbers()
    if not nums:
        print("No valid numbers.")
    else:
        desc = sorted(nums, reverse=True)
        asc = sorted(nums)
        print("Descending:", " ".join(str(n) for n in desc))
        print("Ascending:", " ".join(str(n) for n in asc))
