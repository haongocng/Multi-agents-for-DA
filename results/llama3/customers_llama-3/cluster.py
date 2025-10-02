import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('Customers.csv', encoding='utf-8')

# Select the columns that are relevant for clustering
features_to_cluster = df[['Age', 'Annual Income ($)', 'Spending Score (1-100)']]

# Scale the features using StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_to_cluster)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Find the optimal number of clusters (where the rate of decrease of inertia becomes less steep)
optimal_n_clusters = inertia.index(min(inertia)) + 1

# Apply K-Means Clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Analyze the clusters
print(df.groupby('cluster')[['Age', 'Annual Income ($)', 'Spending Score (1-100)']].mean())