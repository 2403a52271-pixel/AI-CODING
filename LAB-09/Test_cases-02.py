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

# Test cases for assign_grade(score)
test_cases = [
    # Boundary and typical values for each grade
    (100, "A"),
    (99, "A"),
    (90, "A"),
    (89, "B"),
    (80, "B"),
    (79, "C"),
    (70, "C"),
    (69, "D"),
    (60, "D"),
    (59, "F"),
    (0, "F"),
    (50, "F"),
    # Just outside valid range
    (-1, "Invalid input"),
    (-5, "Invalid input"),
    (101, "Invalid input"),
    (105, "Invalid input"),
    # Non-integer/float types
    ("90", "Invalid input"),
    ("eighty", "Invalid input"),
    (None, "Invalid input"),
    ([], "Invalid input"),
    ({}, "Invalid input"),
    (90.0, "A"),
    (89.9, "B"),
    (79.5, "C"),
    (69.99, "D"),
    (59.99, "F"),
]

print("Testing assign_grade(score):")
for score, expected in test_cases:
    result = assign_grade(score)
    print(f"assign_grade({score!r:8}) => {result!r:13} | Expected: {expected!r:13} | {'PASS' if result == expected else 'FAIL'}")
