import pandas as pd

df = pd.read_csv('sampled_dataset.csv', encoding='utf-8')

df = df[df['label'] != 'label']  # Remove erroneous row
df['label'] = df['label'].astype(int)  # Convert label to integer

# Check class distribution
print('Class distribution:')
print(df['label'].value_counts())

# Calculate correlation (only numeric columns, but label is binary)
print('\nCorrelation matrix (label vs. binary encoding):')
print(df[['label']].corr())