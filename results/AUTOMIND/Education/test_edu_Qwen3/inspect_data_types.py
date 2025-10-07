import pandas as pd

# Load the transformed dataset to inspect columns
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Check data types and identify non-numeric columns
print('Data types of all columns:')
print(df.dtypes)

# Identify columns that are object (string) type
string_columns = df.select_dtypes(include=['object']).columns.tolist()
print('\nString columns (to be dropped):')
print(string_columns)