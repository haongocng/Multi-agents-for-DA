import pandas as pd

# Load the data
file_path = 'Customers.csv'
data = pd.read_csv(file_path)

# Select numerical features for clustering
feature_columns = ['Age', 'Annual Income ($)', 'Spending Score (1-100)']
X = data[feature_columns]

# Save the selected features to a new CSV file for use in next steps
X.to_csv('transformed_data.csv', index=False)

# Display the first few rows of the transformed data
X.head()