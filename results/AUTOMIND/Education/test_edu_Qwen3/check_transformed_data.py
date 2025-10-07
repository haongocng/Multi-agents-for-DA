import pandas as pd

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Display the first few rows and column names to understand the structure
print(transformed_data.head())
print("\nColumn names:")
print(transformed_data.columns.tolist())