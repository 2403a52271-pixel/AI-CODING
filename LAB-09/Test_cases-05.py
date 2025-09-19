# AI-generated test cases for convert_date_format(date_str)
def convert_date_format(date_str):
    """Convert date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format."""
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"
def test_convert_date_format():
    print("Testing convert_date_format(date_str):")
    test_cases = [
        # Standard cases
        ("2023-10-15", "15-10-2023"),
        ("1999-01-05", "05-01-1999"),
        ("2000-12-31", "31-12-2000"),
        ("2020-02-29", "29-02-2020"),  # Leap year
        ("1980-07-04", "04-07-1980"),
        ("2021-11-09", "09-11-2021"),
        ("0001-01-01", "01-01-0001"),  # Earliest possible date
        ("2099-09-09", "09-09-2099"),
        ("2010-10-01", "01-10-2010"),
        ("2022-12-25", "25-12-2022"),
        # Edge cases
        ("2023-01-01", "01-01-2023"),
        ("2023-12-01", "01-12-2023"),
        ("2023-01-31", "31-01-2023"),
        ("2023-12-31", "31-12-2023"),
        # Invalid formats
        ("2023/10/15", ValueError),
        ("15-10-2023", ValueError),
        ("2023-10", ValueError),
        ("2023-10-15-01", ValueError),
        ("", ValueError),
        ("20231015", ValueError),
        ("2023-13-01", "01-13-2023"),  # Invalid month, but function does not validate
        ("2023-00-10", "10-00-2023"),  # Invalid month, but function does not validate
        ("2023-02-30", "30-02-2023"),  # Invalid day, but function does not validate
    ]
    for i, (input_str, expected) in enumerate(test_cases, 1):
        try:
            result = convert_date_format(input_str)
            if isinstance(expected, type) and issubclass(expected, Exception):
                print(f"Test {i}: Input: {input_str!r:12} | Expected Exception {expected.__name__} | Got: {result!r} | FAIL")
            else:
                passed = result == expected
                print(f"Test {i}: Input: {input_str!r:12} | Expected: {expected!r:12} | Got: {result!r:12} | {'PASS' if passed else 'FAIL'}")
        except Exception as e:
            if isinstance(expected, type) and isinstance(e, expected):
                print(f"Test {i}: Input: {input_str!r:12} | Expected Exception {expected.__name__} | Got Exception {type(e).__name__} | PASS")
            else:
                print(f"Test {i}: Input: {input_str!r:12} | Expected: {expected!r} | Got Exception {type(e).__name__}: {e} | FAIL")
if __name__ == "__main__":
    test_convert_date_format()
