import pandas as pd
data = {
    'PostID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Likes': [50, 100, 50, 200, 150, 100, 50, 200, 100, 150]
}
df = pd.DataFrame(data)
likes_frequency = df['Likes'].value_counts()
print("Frequency distribution of likes among posts:")
print(likes_frequency)
