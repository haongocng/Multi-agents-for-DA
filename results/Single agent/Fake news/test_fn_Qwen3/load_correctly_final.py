import pandas as pd

# Load the sampled dataset with header and comma separator
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep=',')

# Display basic info
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())

# Check first few rows
print("\nFirst 5 rows:")
print(df.head())

# Check class distribution
print("\nClass distribution:")
print(df['label'].value_counts())

# Verify no missing values
print("\nMissing values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv('cleaned_sampled_dataset.csv', index=False)