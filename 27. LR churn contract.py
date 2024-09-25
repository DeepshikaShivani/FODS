import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('customer_data.csv')
X = data[['usage_minutes', 'contract_duration']] 
y = data['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
usage_minutes = float(input("Enter the usage minutes: "))
contract_duration = float(input("Enter the contract duration (in months): "))
new_customer = np.array([[usage_minutes, contract_duration]])
predicted_churn = model.predict(new_customer)
if predicted_churn[0] == 1:
    print("The customer is predicted to churn.")
else:
    print("The customer is predicted not to churn.")
