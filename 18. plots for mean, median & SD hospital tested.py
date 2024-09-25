import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
data = {
    'Age': [23, 25, 22, 34, 45, 28, 35, 44, 36, 52, 30, 48, 50, 27, 29, 46, 39, 33],
    '%Fat': [14.1, 13.2, 10.9, 23.3, 28.7, 18.4, 20.9, 27.6, 22.1, 30.1, 16.7, 25.6, 28.1, 17.2, 19.5, 26.7, 21.2, 24.8]
}
df = pd.DataFrame(data)
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_fat = df['%Fat'].mean()
median_fat = df['%Fat'].median()
std_fat = df['%Fat'].std()

print(f"Age - Mean: {mean_age}, Median: {median_age}, Standard Deviation: {std_age}")
print(f"%Fat - Mean: {mean_fat}, Median: {median_fat}, Standard Deviation: {std_fat}")

# Boxplots
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(df['Age']).set_title('Boxplot of Age')
plt.subplot(1, 2, 2)
sns.boxplot(df['%Fat']).set_title('Boxplot of %Fat')
plt.show()

# Scatter plot
plt.scatter(df['Age'], df['%Fat'])
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.title('Scatter plot of Age vs %Fat')
plt.show()

# Q-Q plot for Age and %Fat
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q plot of Age')
plt.subplot(1, 2, 2)
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title('Q-Q plot of %Fat')
plt.show()
