import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Load scaled data
df_scaled = pd.read_csv('transformed_data.csv')

# Define feature columns
feature_cols = ['Gender', 'Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Profession', 'Work Experience', 'Family Size']
X = df_scaled[feature_cols]

# Use Elbow Method to find optimal K
inertias = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Plot Elbow
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.savefig('elbow_plot.png')
plt.close()

# Choose K=5 based on elbow and domain knowledge
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df_scaled['Cluster'] = kmeans.fit_predict(X)

# Save clustered data
df_scaled.to_csv('clustered_data.csv', index=False)

# Save model
import joblib
joblib.dump(kmeans, 'kmeans_model.pkl')

# Print cluster sizes
print("Cluster sizes:")
print(df_scaled['Cluster'].value_counts().sort_index())

# Print cluster centers (scaled)
cluster_centers = kmeans.cluster_centers_
print("\nCluster Centers (scaled):")
for i, center in enumerate(cluster_centers):
    print(f"Cluster {i}: {center}")