def ai_loan_approval(applicant_name, income, credit_score):
    if applicant_name.lower() == "john":
        if income >= 30000 and credit_score >= 600:
            return "Approved"
        else:
            return "Denied"
    elif applicant_name.lower() == "priya":
        if income >= 50000 and credit_score >= 700:
            return "Approved"
        else:
            return "Denied"
    else:
        if income >= 40000 and credit_score >= 650:
            return "Approved"
        else:
            return "Denied"
applicants = [
    {"name": "John", "income": 35000, "credit_score": 620},
    {"name": "Priya", "income": 35000, "credit_score": 620},
    {"name": "Alex", "income": 35000, "credit_score": 620},
]
for applicant in applicants:
    result = ai_loan_approval(applicant["name"], applicant["income"], applicant["credit_score"])
    print(f"Loan approval for {applicant['name']}: {result}")