import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame({
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Scores': [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
})
print(data.head())
correlation = data['Study_Hours'].corr(data['Exam_Scores'])
print(f'Correlation Coefficient: {correlation:.2f}')
plt.figure(figsize=(10, 6))
plt.scatter(data['Study_Hours'], data['Exam_Scores'], color='blue')
plt.title('Scatter Plot of Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid()
plt.show()
plt.figure(figsize=(10, 6))
sns.regplot(x='Study_Hours', y='Exam_Scores', data=data, color='orange', marker='o')
plt.title('Study Hours vs Exam Scores with Regression Line')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid()
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='Study_Hours', y='Exam_Scores', data=data, palette='Set3')
plt.title('Box Plot of Exam Scores by Study Hours')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid()
plt.show()
correlation_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
