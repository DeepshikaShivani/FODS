import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('housing_data.csv')
X = data[['area', 'bedrooms']] 
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
area = float(input("Enter the area of the house (in square feet): "))
bedrooms = int(input("Enter the number of bedrooms: "))
new_house = np.array([[area, bedrooms]])
predicted_price = model.predict(new_house)
print(f"The predicted price of the house is: ${predicted_price[0]:,.2f}")
