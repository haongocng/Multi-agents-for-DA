import pandas as pd

# Load the sampled dataset with no header
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first 10 rows to inspect raw values
print("First 10 rows of raw data:")
print(df.head(10))

# Check the type of the first data row
print("\nType of first data row (index 1):", type(df.iloc[1, 0]))
print("Content of first data row:", df.iloc[1, 0])

# Check if there are any empty or malformed rows
print("\nNumber of rows with no comma:", (df[0].str.contains(',') == False).sum())

# Show first 5 rows after split to see what's happening
df_split = df[0].str.split(',', n=1, expand=True)
df_split.columns = ['text', 'label']

# Check for NaN in label
print("\nNumber of NaN in label column:", df_split['label'].isna().sum())

# Show the first 5 rows of the split dataframe
print("\nFirst 5 rows of split dataframe:")
print(df_split.head())