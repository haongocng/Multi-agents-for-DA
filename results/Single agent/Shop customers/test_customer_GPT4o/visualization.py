import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the clustered data
clustered_data = pd.read_csv('clustered_data.csv')

# Select features for PCA
features = clustered_data[['Age', 'Annual Income ($)', 'Spending Score (1-100)']]

# Apply PCA to reduce dimensions to 2D for visualization
pca = PCA(n_components=2)
components = pca.fit_transform(features)

# Create a DataFrame with the PCA components
pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
pca_df['Cluster'] = clustered_data['Cluster']

# Plot the clusters
plt.figure(figsize=(10, 7))
for cluster in pca_df['Cluster'].unique():
    cluster_data = pca_df[pca_df['Cluster'] == cluster]
    plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')

plt.title('Customer Segments Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)
plt.savefig('clusters_visualization.png')
plt.show()