import pandas as pd

# Load the sampled dataset with correct encoding
filepath = 'sampled_dataset.csv'
df = pd.read_csv(filepath, encoding='utf-8')

# Check unique values in the label column
print("Unique values in 'label' column before cleaning:", df['label'].unique())

# Remove rows where label == 'label' (header contamination)
df = df[df['label'] != 'label']

# Convert remaining labels to binary: '0' -> 0, '1' -> 1
df['label'] = df['label'].map({'0': 0, '1': 1})

# Verify transformation
print("Unique values in 'label' column after cleaning:", df['label'].unique())
print("Class distribution after cleaning:", df['label'].value_counts())

# Save transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Print summary of transformed data
print("\nInfo of transformed DataFrame:")
df.info()