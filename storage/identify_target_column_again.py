import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Print the column names to identify the correct target column
target_column_prefix = 'I am willing to share my digital skills with other students'
target_column = [col for col in df.columns if col.startswith(target_column_prefix)]

if not target_column:
    print("Target column not found. Searching for a similar column...")
    # Search for a column that might represent the target variable
    for col in df.columns:
        if 'share' in col or 'digital' in col or 'skills' in col:
            print(f'Potential target column: {col}')

# Print the identified target column name
print(f'Target Column: {target_column if target_column else 'Not Found'}')