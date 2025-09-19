import string

def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    print("Examples:")
    examples = [
        "Step on no pets.",
        "Was it a car or a cat I saw?",
        "Hello, Python!",
        "Never odd or even.",
        "Not a palindrome"
    ]
    for example in examples:
        result = is_sentence_palindrome(example)
        print(f"'{example}' -> Palindrome? {result}")