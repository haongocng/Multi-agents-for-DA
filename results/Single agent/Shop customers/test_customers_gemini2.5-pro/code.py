
import pandas as pd

df = pd.read_csv("original_clustered_data.csv")

cluster_profiles = df.groupby('Cluster').agg({
    'Age': ['mean', 'std'],
    'Annual Income ($)': ['mean', 'std'],
    'Spending Score (1-100)': ['mean', 'std'],
    'Gender': lambda x: x.value_counts().index[0],
    'Work Experience': ['mean', 'std'],
    'Family Size': ['mean', 'std'],
    'Profession': lambda x: x.value_counts().index[0]
}).round(2)

print("Cluster Profiles:")
print(cluster_profiles)
