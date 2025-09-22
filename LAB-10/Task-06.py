def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage:
scores = [95, 82, 76, 65, 50]
for s in scores:
    print(f"Score: {s} => Grade: {grade(s)}")

