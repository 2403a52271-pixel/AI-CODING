import pandas as pd
import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (only first run)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# File paths
file_path = r"C:\Users\owner\OneDrive\Desktop\AI ASSISTED CODING\Lab 17.4\social_media_data.csv"
output_path = r"C:\Users\owner\OneDrive\Desktop\AI ASSISTED CODING\Lab 17.4\cleaned_social_media_data.csv"

# ✅ Create sample CSV automatically if missing
if not os.path.exists(file_path):
    sample_data = """username,text
user1,I love this product! 😊
user2,Worst service ever... 😡
user3,Totally worth the price! 💯
user4,Not bad, but could be better.
user5,The delivery was super fast! 🚀
user6,I will never buy from here again 😠
user7,Absolutely amazing service 😍
user8,Okayish experience, nothing special 🤷‍♀️
user9,Refund process was quick and smooth 👍
user10,Very disappointed 😢
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(sample_data)
    print(f"📁 Sample dataset created at: {file_path}")

# Load dataset
df = pd.read_csv(file_path)

# Text cleaning function
def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', str(text))  # remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)          # remove special chars & emojis
    return text.lower()                              # lowercase

df['clean_text'] = df['text'].apply(clean_text)

# Tokenization, stopword removal, lemmatization
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

df['clean_text'] = df['clean_text'].apply(preprocess)

# Save cleaned dataset
df.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved successfully at: {output_path}")

