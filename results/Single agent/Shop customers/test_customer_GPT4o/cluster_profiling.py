import pandas as pd

# Load the clustered data
clustered_data = pd.read_csv('clustered_data.csv')

# Analyze the characteristics of each cluster
cluster_profiles = clustered_data.groupby('Cluster').agg({
    'Age': ['mean', 'min', 'max'],
    'Annual Income ($)': ['mean', 'min', 'max'],
    'Spending Score (1-100)': ['mean', 'min', 'max'],
    'Gender': lambda x: x.mode()[0],
    'Profession': lambda x: x.mode()[0],
    'Work Experience': ['mean', 'min', 'max'],
    'Family Size': ['mean', 'min', 'max']
}).reset_index()

# Convert the multi-level columns to single level
cluster_profiles.columns = ['_'.join(col).strip() for col in cluster_profiles.columns.values]

cluster_profiles