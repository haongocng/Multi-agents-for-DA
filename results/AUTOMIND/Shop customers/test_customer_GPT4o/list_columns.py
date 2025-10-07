import pandas as pd

# Load the transformed dataset to check column names
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Print the column names to identify the correct ones for clustering
print(df.columns.tolist())