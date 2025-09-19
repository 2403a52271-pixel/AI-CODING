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
# Test cases for is_valid_email and validator
test_emails = [
    # Valid cases
    ("user@example.com", "Valid"),
    ("john.doe@mail.co.uk", "Valid"),
    ("a@b.c", "Valid"),
    ("user.name@domain.com", "Valid"),
    ("user@example.co.in", "Valid"),
    # Invalid: missing '@'
    ("user.example.com", "Invalid"),
    # Invalid: missing '.'
    ("user@examplecom", "Invalid"),
    # Invalid: multiple '@'
    ("user@@example.com", "Invalid"),
    ("user@ex@ample.com", "Invalid"),
    # Invalid: starts with '@'
    ("@userexample.com", "Invalid"),
    # Invalid: ends with '@'
    ("userexample.com@", "Invalid"),
    # Invalid: starts with '.'
    (".user@example.com", "Invalid"),
    # Invalid: ends with '.'
    ("user@example.com.", "Invalid"),
    # Invalid: only special characters
    ("@.", "Invalid"),
    # Invalid: empty string
    ("", "Invalid"),
    # Invalid: only '@'
    ("@", "Invalid"),
    # Invalid: only '.'
    (".", "Invalid"),
    # Valid: numbers and underscores
    ("user_123@domain.co", "Valid"),
    # Invalid: space in email
    ("user @example.com", "Invalid"),
    ("user@ example.com", "Invalid"),
    ("user@example. com", "Invalid"),
]

for email, expected in test_emails:
    result = validator(email)
    print(f"Testing: {email!r:25} Expected: {expected:7} Got: {result:7} {'PASS' if result == expected else 'FAIL'}")
