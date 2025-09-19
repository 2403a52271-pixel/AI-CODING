def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
# AI-generated test cases for is_sentence_palindrome(sentence)
test_cases = [
    # Classic palindromes
    ("A man, a plan, a canal: Panama", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("Step on no pets.", True),
    ("Never odd or even.", True),
    ("Eva, can I see bees in a cave?", True),
    ("Madam In Eden, I’m Adam", True),
    ("Able was I, I saw Elba", True),
    ("Mr. Owl ate my metal worm", True),
    ("Do geese see God?", True),
    ("Murder for a jar of red rum", True),
    ("Go hang a salami, I'm a lasagna hog", True),
    ("Red roses run no risk, sir, on Nurse's order.", True),
    ("Was it a car or a cat I saw", True),
    ("A Toyota's a Toyota", True),
    ("", True),  # Empty string is a palindrome
    # Not palindromes
    ("Hello, World!", False),
    ("Python is fun", False),
    ("Palindrome", False),
    ("This is not a palindrome", False),
    ("Almostomla", False),
    ("Step on no pets today.", False),
    ("Was it a dog or a cat I saw?", False),
    ("Never even or odd.", False),
    ("Eva, can I see bees in a cave", False),  # missing punctuation, but not a palindrome
    ("Go hang a salami, I'm a lasagna dog", False),
    # Edge cases
    ("A", True),  # Single character
    ("aa", True),
    ("ab", False),
    ("12321", True),
    ("12345", False),
    ("1 2 3 2 1", True),
    ("1,2,3,4,5", False),
    ("!@#$%^&*()", True),  # Only punctuation, cleaned is empty, so palindrome
    ("   ", True),  # Only spaces, cleaned is empty, so palindrome
]
print("Testing is_sentence_palindrome(sentence):")
for sentence, expected in test_cases:
    result = is_sentence_palindrome(sentence)
    print(f"Input: {sentence!r:40} | Expected: {expected!s:5} | Got: {result!s:5} | {'PASS' if result == expected else 'FAIL'}")
