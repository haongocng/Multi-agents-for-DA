import pandas as pd

# Load the sampled dataset
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')

# Clean the label column: remove rows where label is not '0' or '1'
df = df[df['label'].isin(['0', '1'])]

# Convert label to integer
df['label'] = df['label'].astype(int)

# Text preprocessing: lowercase and remove special characters (keep only letters and spaces)
df['text'] = df['text'].str.lower().str.replace(r'[^a-zA-Z\s]', '', regex=True)

# Check for any remaining missing values after cleaning
df = df.dropna(subset=['text'])

# Save cleaned and preprocessed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Print summary
print("Cleaned and preprocessed data shape:", df.shape)
print("Label distribution:\n", df['label'].value_counts())
print("\nFirst few rows of transformed data:")
print(df.head())