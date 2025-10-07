import pandas as pd
# Load the sampled dataset
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')
# Perform initial data exploration
print('Data Shape:', df.shape)
print('Data Columns:', df.columns)
print('Data Types:\n', df.dtypes)
print('Data Sample:\n', df.head())
# Save EDA report to file
with open('eda_report.txt', 'w') as f:
    f.write(str(df.shape))
    f.write(str(df.columns))
    f.write(str(df.dtypes))
    f.write(str(df.head()))