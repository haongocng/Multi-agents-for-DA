import pandas as pd

# Check the full shape and encoding of train.csv
df = pd.read_csv('train.csv', encoding='utf-8', sep='\t')
print(f"Shape of train.csv: {df.shape}")
print(f"Column names: {list(df.columns)}")
print(f"Unique values in label: {df['label'].unique()}")
print(f"Data types:\n{df.dtypes}")