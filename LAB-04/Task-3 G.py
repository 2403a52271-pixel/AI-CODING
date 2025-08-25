def parse_student_info(student: dict) -> str:
    first_name = student["personal"]["first_name"]
    last_name = student["personal"]["last_name"]
    branch = student["academic"]["branch"]
    sgpa = student["academic"]["sgpa"]
    return f"Full Name: {first_name} {last_name}, Branch: {branch}, SGPA: {sgpa}"

# Test cases from few-shot examples
student1 = {
    "personal": {"first_name": "Amit", "last_name": "Sharma"},
    "academic": {"branch": "CSE", "sgpa": 8.7}
}

student2 = {
    "personal": {"first_name": "Riya", "last_name": "Verma"},
    "academic": {"branch": "ECE", "sgpa": 9.2}
}

print(parse_student_info(student1))  # Full Name: Amit Sharma, Branch: CSE, SGPA: 8.7
print(parse_student_info(student2))  # Full Name: Riya Verma, Branch: ECE, SGPA: 9.2