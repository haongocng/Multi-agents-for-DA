import pandas as pd

# Load the dataset as single column and split by the first comma only
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Split the first column by the first comma to separate text and label
df_split = df[0].str.split(',', n=1, expand=True)

# Set column names
df_split.columns = ['text', 'label']

# Strip whitespace from both columns
df_split['text'] = df_split['text'].str.strip()
df_split['label'] = df_split['label'].str.strip()

# Convert label to integer
df_split['label'] = df_split['label'].astype(int)

# Display first few rows and class distribution
df_split.head()

df_split['label'].value_counts()