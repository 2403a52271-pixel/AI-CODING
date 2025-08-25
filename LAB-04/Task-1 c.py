import re

def is_valid_indian_mobile(number: str) -> bool:
    pattern = r'^[6-9][0-9]{9}$'
    return bool(re.match(pattern, number))
print(is_valid_indian_mobile("9876543210")) 
    
