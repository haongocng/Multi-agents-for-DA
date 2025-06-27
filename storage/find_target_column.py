import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Find the column name that matches 'I am willing to share my digital skills with other students'
target_column_name = [col for col in df.columns if 'I am willing to share my digital skills with other students' in col]

# Print the matching column name
print(target_column_name)