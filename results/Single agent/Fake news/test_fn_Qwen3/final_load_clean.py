import pandas as pd

# Load the sampled dataset with no header
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Remove the header row (first row)
df = df.iloc[1:].reset_index(drop=True)

# Split the remaining rows on the first comma only
df_split = df[0].str.split(',', n=1, expand=True)

# Assign column names
df_split.columns = ['text', 'label']

# Strip whitespace from both columns
df_split['text'] = df_split['text'].str.strip()
df_split['label'] = df_split['label'].str.strip()

# Check for any remaining empty or NaN labels
print("Number of NaN in label column:", df_split['label'].isna().sum())
print("Number of empty strings in label column:", df_split['label'].eq('').sum())

# Convert label to integer (only for non-empty values)
df_split = df_split.dropna(subset=['label'])
df_split['label'] = df_split['label'].astype(int)

# Verify the cleaned dataset
print("\nFinal dataset shape:", df_split.shape)
print("\nFirst 5 rows:")
print(df_split.head())

# Check class distribution
class_dist = df_split['label'].value_counts()
print("\nClass distribution:")
print(class_dist)

# Save cleaned sample data
df_split.to_csv('cleaned_sampled_dataset.csv', index=False)