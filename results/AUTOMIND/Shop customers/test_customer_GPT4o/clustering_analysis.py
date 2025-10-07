import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Select features for clustering
features_to_cluster = df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']]

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_to_cluster)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method For Optimal N_CLUSTERS')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.savefig('elbow_method.png')
plt.close()

# Based on the plot, choose the N_CLUSTERS where the inertia starts to decrease slowly.
# For this example, let's assume the optimal number of clusters is 5
optimal_n_clusters = 5
kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Analyze cluster characteristics
cluster_characteristics = df.groupby('cluster').mean()
cluster_characteristics.to_csv('cluster_characteristics.csv')

# Further analysis like value counts for categorical features within each cluster
# Assuming there are categorical columns in the original dataset
cluster_gender_distribution = df.groupby('cluster')[['Gender_Female', 'Gender_Male']].mean()
cluster_gender_distribution.to_csv('cluster_gender_distribution.csv')

print(cluster_characteristics)
print(cluster_gender_distribution)