from collections import Counter
import re
reviews = [
    "Great product! Highly recommend it.",
    "Good quality, but the delivery was late.",
    "Not satisfied with the product. Poor customer service.",
    "Excellent quality and fast delivery!",
    "Product is okay, but packaging was damaged."
]
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text
processed_reviews = [preprocess_text(review) for review in reviews]
words = []
for review in processed_reviews:
    words.extend(review.split())
word_freq = Counter(words)
print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
