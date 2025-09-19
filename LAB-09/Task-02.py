def assign_grade(score):
    # Check for invalid input types
    if not isinstance(score, (int, float)):
        return "Invalid input"
    # Check for out-of-range values
    if score < 0 or score > 100:
        return "Invalid input"
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"
examples = [
    (92, "A"),
    (88, "B"),
    (73, "C"),
    (67, "D"),
    (50, "F"),
    (-1, "Invalid input"),
    (101, "Invalid input"),
    ("90", "Invalid input"),
    (None, "Invalid input"),
]

print(" Example Test Cases:")
for score, expected in examples:
    result = assign_grade(score)
    print(f"assign_grade({score!r}) => {result!r} | Expected: {expected!r} | {'PASS' if result == expected else 'FAIL'}")


