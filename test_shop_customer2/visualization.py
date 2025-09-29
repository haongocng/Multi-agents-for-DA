import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Load clustered data
df_clustered = pd.read_csv('clustered_data.csv')

# Select features for visualization (excluding Cluster)
feature_cols = ['Gender', 'Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Profession', 'Work Experience', 'Family Size']
X = df_clustered[feature_cols]

# Reduce to 2D for visualization using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['Cluster'] = df_clustered['Cluster']

# Plot PCA visualization
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='Cluster', palette='deep', s=60)
plt.title('Customer Segments: PCA of 7 Features (2D)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend(title='Cluster')
plt.grid(True, alpha=0.3)
plt.savefig('pca_cluster_plot.png')
plt.close()

# Create pairplot for key features only (Age, Income, Spending)
key_features = ['Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Cluster']
df_key = df_clustered[key_features]
sns.pairplot(df_key, hue='Cluster', palette='deep')
plt.savefig('pairplot_clusters.png')
plt.close()

print("Visualization plots saved: pca_cluster_plot.png, pairplot_clusters.png")