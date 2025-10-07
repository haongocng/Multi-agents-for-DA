import pandas as pd

# Load the sampled dataset
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', sep='\t')

# Check column names
print("Column names:", df.columns.tolist())

# Check class distribution
label_counts = df['label'].value_counts()

# Check text length statistics
df['text_length'] = df['text'].str.len()
text_length_stats = df['text_length'].describe()

# Display results
label_counts, text_length_stats