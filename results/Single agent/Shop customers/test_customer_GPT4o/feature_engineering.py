import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset again
file_path = 'Customers.csv'
data = pd.read_csv(file_path)

# Select relevant features for clustering
features = data[['Age', 'Annual Income ($)', 'Spending Score (1-100)']]

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Create a DataFrame with the scaled features
scaled_data = pd.DataFrame(scaled_features, columns=features.columns)

# Save the transformed data
scaled_data.to_csv('transformed_data.csv', index=False)

scaled_data.head()