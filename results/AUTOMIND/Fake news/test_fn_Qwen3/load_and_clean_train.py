import pandas as pd

# Load the full training dataset with confirmed parameters
df = pd.read_csv('train.csv', encoding='utf-8', sep='\t')

# Defensive cleaning: remove rows where label == 'label'
df = df[df['label'] != 'label']

# Convert label to binary integers
df['label'] = df['label'].map({'0': 0, '1': 1})

# Confirm transformation
print(f"Dataset shape after cleaning: {df.shape}")
print(f"Label distribution:\n{df['label'].value_counts()}")