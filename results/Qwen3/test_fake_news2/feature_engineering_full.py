import pandas as pd

# Load the full train.csv with correct separator and encoding
df = pd.read_csv('train.csv', encoding='utf-8', sep='\t')

# Clean the data: remove rows where label == 'label'
df = df[df['label'] != 'label']

# Convert label to integer
df['label'] = df['label'].astype(int)

# Text preprocessing: lowercase and remove non-alphanumeric characters (keep letters, digits, spaces)
df['text'] = df['text'].astype(str).str.lower().str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# Save the fully transformed dataset
df.to_csv('full_transformed_train.csv', index=False, encoding='utf-8')

# Print summary
print("Full transformed dataset shape:", df.shape)
print("Label distribution:\n", df['label'].value_counts())
print("\nFirst few rows of transformed data:")
print(df.head())