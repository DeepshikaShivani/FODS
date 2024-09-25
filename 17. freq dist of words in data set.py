import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data['feedback']
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words
def calculate_word_frequency(feedback_list):
    all_words = []
    for feedback in feedback_list:
        all_words.extend(preprocess_text(feedback))
    word_freq = Counter(all_words)
    return word_freq
def display_top_words(word_freq, N):
    most_common_words = word_freq.most_common(N)
    print(f"Top {N} most frequent words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")
    return most_common_words
def plot_word_frequency(word_freq, N):
    words, frequencies = zip(*word_freq)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title(f'Top {N} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.show()
def main():
    file_path = 'data.csv'
    feedback_data = load_data(file_path)
    word_freq = calculate_word_frequency(feedback_data)
    N = int(input("Enter the number of top frequent words to display: "))
    top_words = display_top_words(word_freq, N)
    plot_word_frequency(top_words, N)
if __name__ == '__main__':
    main()
