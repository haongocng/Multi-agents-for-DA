import pandas as pd

# Load the sampled dataset with explicit tab separator and inspect column names
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')

# Print column names to confirm
column_names = df.columns.tolist()
print("Column names:", column_names)

# Check for any whitespace in column names
column_names_stripped = [col.strip() for col in column_names]
print("Stripped column names:", column_names_stripped)

# Check the first few rows to verify content
df.head()