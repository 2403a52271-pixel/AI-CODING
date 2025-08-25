import string
from collections import Counter

def most_frequent_word(paragraph):
    # Step 1: Convert text to lowercase
    paragraph = paragraph.lower()
    
    # Step 2: Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    
    # Step 3: Split text into words
    words = paragraph.split()
    
    # Step 4: Count the frequency of each word
    word_counts = Counter(words)
    
    # Step 5: Return the most frequent word
    most_common = word_counts.most_common(1)[0][0]
    
    return most_common

# Example usage:
text = "Data science is fun. Science is powerful. Data is useful."
print("Most frequent word:", most_frequent_word(text))

