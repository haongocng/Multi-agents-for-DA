import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Print the column names to identify the correct target column
target_column_prefix = 'I am willing to share my digital skills with other students'
target_column = [col for col in df.columns if col.startswith(target_column_prefix)]

if target_column:
    target_column = target_column[0]
else:
    target_column = None

# Print the identified target column name
print(f'Target Column: {target_column}')