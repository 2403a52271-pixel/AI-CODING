def convert_date_format(date_str):
    """Convert date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format."""
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

# Example usage:
date1 = "2023-10-15"
date2 = "1999-01-05"
print(convert_date_format(date1))  # Output: 15-10-2023
print(convert_date_format(date2))  # Output: 05-01-1999
