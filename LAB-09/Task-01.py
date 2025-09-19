def is_valid_email(email):
    # Email must contain exactly one '@'
    if email.count('@') != 1:
        return False
    # Email must contain at least one '.'
    if '.' not in email:
        return False
    # Email must not start or end with special characters '@' or '.'
    if email[0] in {'@', '.'} or email[-1] in {'@', '.'}:
        return False
    return True
def validator(email):
    if is_valid_email(email):
        return "Valid"
    else:
        return "Invalid"
# Example usage:
if __name__ == "__main__":
    test_emails = [
        "nivy@email.com",      # Valid
        "amruth.email@com",      # Valid
        "@nivyemail.com",      # Invalid (starts with @)
        "amruthemail.com@",      # Invalid (ends with @)
        "nivy@email.com",   
    ]
    for email in test_emails:
        print(f"{email}: {validator(email)}")

