import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the scaled data
scaled_data = pd.read_csv('transformed_data.csv')

# Determine the optimal number of clusters using the Elbow method
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    sse.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.xticks(range(1, 11))
plt.grid(True)
plt.savefig('elbow_method.png')
plt.show()

# Choose the optimal number of clusters (e.g., 4 based on the elbow method)
optimal_k = 4

# Apply KMeans with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add the cluster labels to the original data
original_data = pd.read_csv('Customers.csv')
original_data['Cluster'] = clusters

# Save the clustered data
original_data.to_csv('clustered_data.csv', index=False)

original_data.head()