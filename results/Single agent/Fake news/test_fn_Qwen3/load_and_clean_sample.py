import pandas as pd

# Load the sampled dataset with no header
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Split the first column on the first comma only
df_split = df[0].str.split(',', n=1, expand=True)

# Assign column names
df_split.columns = ['text', 'label']

# Strip whitespace from both columns
df_split['text'] = df_split['text'].str.strip()
df_split['label'] = df_split['label'].str.strip()

# Convert label to integer
df_split['label'] = df_split['label'].astype(int)

# Verify the data
print("Shape of cleaned dataset:", df_split.shape)
print("\nFirst 5 rows:")
print(df_split.head())

# Check class distribution
class_dist = df_split['label'].value_counts()
print("\nClass distribution:")
print(class_dist)

# Save cleaned sample data
df_split.to_csv('cleaned_sampled_dataset.csv', index=False)