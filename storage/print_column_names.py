import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Print the full list of column names
print(df.columns.tolist())