import pandas as pd
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [25, 30, 22, 25, 30, 40, 22, 35, 30, 25],
    'PurchaseAmount': [200, 150, 300, 450, 200, 500, 350, 600, 250, 400]
}
df = pd.DataFrame(data)
age_frequency = df['Age'].value_counts()
print("Frequency distribution of customer ages:")
print(age_frequency)
