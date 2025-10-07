import pandas as pd

# Load the sampled dataset with no header and manual column assignment
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Use first row as column names
column_names = df.iloc[0].tolist()

# Drop the first row and reset index
df = df.iloc[1:].reset_index(drop=True)

# Assign column names
df.columns = column_names

# Convert label column to integer
df['label'] = df['label'].astype(int)

# Display cleaned dataframe info
df.head()

# Check class distribution
df['label'].value_counts()