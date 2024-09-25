import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('patient_data.csv')
X = data.drop('condition', axis=1) 
y = data['condition'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
k = int(input("Enter the number of neighbors (k): "))
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
new_patient = []
num_features = X.shape[1]
for i in range(num_features):
    feature_value = float(input(f"Enter value for symptom {i + 1}: "))
    new_patient.append(feature_value)
new_patient_scaled = scaler.transform([new_patient])
prediction = knn.predict(new_patient_scaled)
if prediction[0] == 1:
    print("The patient is predicted to have the medical condition.")
else:
    print("The patient is predicted not to have the medical condition.")
