import string
from collections import Counter
def calculate_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = Counter(words)
    for word, count in word_count.items():
        print(f'{word}: {count}')
file_path = 'hiii.txt' 
calculate_word_frequency(file_path)
