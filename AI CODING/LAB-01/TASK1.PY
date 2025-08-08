def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
print(is_palindrome(string))