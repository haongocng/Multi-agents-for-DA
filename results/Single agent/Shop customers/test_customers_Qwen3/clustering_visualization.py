import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load scaled data
X_scaled = pd.read_csv('X_scaled.csv')

# Apply K-Means with k=5 (from elbow method)
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

# Reduce dimensions to 2D using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create scatter plot of clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis', alpha=0.6)
plt.title('K-Means Clustering (k=5) Visualized with PCA')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.savefig('cluster_pca_plot.png')
plt.close()

# Save cluster labels back to original data for profiling
original_data = pd.read_csv('Customers.csv')
original_data['Cluster'] = cluster_labels
original_data.to_csv('Customers_with_clusters.csv', index=False)

# Output cluster centers (in scaled space)
cluster_centers_scaled = kmeans.cluster_centers_
cluster_centers_scaled