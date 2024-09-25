import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('transaction_data.csv')
print(data.head())
X = data[['TotalAmountSpent', 'NumberOfItemsPurchased']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.grid()
plt.show()
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)
plt.figure(figsize=(10, 6))
plt.scatter(data['TotalAmountSpent'], data['NumberOfItemsPurchased'], c=data['Cluster'], cmap='viridis', marker='o')
plt.title('Customer Segments based on Spending and Purchase Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()
cluster_summary = data.groupby('Cluster')[['TotalAmountSpent', 'NumberOfItemsPurchased']].mean().reset_index()
print("\nCluster Summary:")
print(cluster_summary)
