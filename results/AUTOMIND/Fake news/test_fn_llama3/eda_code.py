import pandas as pd
# Load the sampled dataset
sampled_data_path = 'sampled_dataset.csv'
df = pd.read_csv(sampled_data_path, encoding='utf-8', sep='\t')
# Get shape
shape = df.shape
# Get data types
data_types = df.dtypes
# Get concise summary
info = df.info()
# Get descriptive statistics
describe = df.describe(include='all')
# Value counts for categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
value_counts = {}
for col in categorical_cols:
    value_counts[col] = df[col].value_counts()
# Handling missing values
missing_values = df.isnull().sum()
# Save EDA report to a file
def save_eda_report(shape, data_types, info, describe, value_counts, missing_values):
    with open('eda_report.txt', 'w') as f:
        f.write(f'Shape: {shape}\n')
        f.write(f'Data Types:\n{data_types}\n')
        f.write(f'Info:\n{info}\n')
        f.write(f'Descriptive Statistics:\n{describe}\n')
        f.write(f'Value Counts for Categorical Columns:\n{value_counts}\n')
        f.write(f'Missing Values:\n{missing_values}\n')
save_eda_report(shape, data_types, info, describe, value_counts, missing_values)
# Output a concise summary string
print('EDA report saved to eda_report.txt')