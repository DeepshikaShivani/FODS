import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text
data = pd.read_csv('used_cars.csv')
features = ['mileage', 'age', 'brand', 'engine_type']
target = 'price'
X = data[features]
y = data[target]
X = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
mileage = float(input("Enter the mileage of the car: "))
age = float(input("Enter the age of the car: "))
brand = input("Enter the brand of the car: ")
engine_type = input("Enter the engine type of the car: ")
new_car = pd.DataFrame([[mileage, age, brand, engine_type]], columns=features)
new_car = pd.get_dummies(new_car, drop_first=True)
new_car = new_car.reindex(columns=X.columns, fill_value=0)
predicted_price = model.predict(new_car)[0]
print(f"The predicted price of the car is: ${predicted_price:.2f}")decision_tree_text = export_text(model, feature_names=list(X.columns))
print("\nDecision path for the prediction:\n")
print(decision_tree_text)
