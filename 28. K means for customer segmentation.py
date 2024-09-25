import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('customer_data.csv')
X = data[['spending_score', 'annual_income']] 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
k = 3  
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)
spending_score = float(input("Enter the spending score of the customer: "))
annual_income = float(input("Enter the annual income of the customer: "))
new_customer = np.array([[spending_score, annual_income]])
new_customer_scaled = scaler.transform(new_customer)
predicted_segment = kmeans.predict(new_customer_scaled)
print(f"The new customer is assigned to segment: {predicted_segment[0]}")
