import pandas as pd

# Load the sampled dataset with explicit tab separator
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')

# Since column name is 'text,label', split it into two columns
df_split = df['text,label'].str.split(',', n=1, expand=True)
df_split.columns = ['text', 'label']

# Convert label to integer
df_split['label'] = df_split['label'].astype(int)

# Display the cleaned dataframe
df_split.head()

# Check class distribution
df_split['label'].value_counts()