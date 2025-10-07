import pandas as pd

# Load the sampled dataset with no header
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first 10 rows to inspect raw values
df.head(10)

# Check if any row has empty label after split
print("\nChecking the label column after split:")

df_split = df[0].str.split(',', n=1, expand=True)
df_split.columns = ['text', 'label']

# Strip whitespace
df_split['label'] = df_split['label'].str.strip()

# Check for NaN or empty strings in label
df_split['label'].isna().sum(), df_split['label'].eq('').sum()

# Show unique values in label column
print("\nUnique label values:")
df_split['label'].unique()