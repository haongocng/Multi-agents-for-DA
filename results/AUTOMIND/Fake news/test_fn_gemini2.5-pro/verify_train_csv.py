import pandas as pd

df = pd.read_csv('train.csv', encoding='latin1', sep='\t')

print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

print("\nLabel distribution:")
print(df['label'].value_counts())