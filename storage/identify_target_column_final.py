import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv')

# Print the column names to identify the correct target column
potential_target_columns = [col for col in df.columns if 'share' in col or 'digital' in col or 'skills' in col]

if potential_target_columns:
    print(f'Potential target columns: {potential_target_columns}')
else:
    print('No potential target columns found.')