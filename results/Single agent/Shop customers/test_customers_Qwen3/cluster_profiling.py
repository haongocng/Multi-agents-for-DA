import pandas as pd

# Load the dataset with cluster labels
file_path = 'Customers_with_clusters.csv'
data = pd.read_csv(file_path)

# Define the numerical features used for clustering
feature_columns = ['Age', 'Annual Income ($)', 'Spending Score (1-100)']

# Group by cluster and compute mean for each feature and categorical variables
cluster_profiles = data.groupby('Cluster')[feature_columns + ['Gender', 'Profession']].agg({
    'Age': 'mean',
    'Annual Income ($)': 'mean',
    'Spending Score (1-100)': 'mean',
    'Gender': lambda x: x.mode()[0],  # Most frequent gender
    'Profession': lambda x: x.mode()[0]  # Most frequent profession
}).round(2)

# Count the number of customers in each cluster
cluster_sizes = data['Cluster'].value_counts().sort_index()
cluster_profiles['Customer Count'] = cluster_sizes

# Display the cluster profiles
cluster_profiles