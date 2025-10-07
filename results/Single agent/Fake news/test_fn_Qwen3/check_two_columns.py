import pandas as pd

# Load the sampled dataset with no header
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first 10 rows to inspect
print("First 10 rows of raw data:")
print(df.head(10))

# Check if the label is in the second column (index 1)
print("\nChecking second column (index 1) values:")
print(df.iloc[1:, 1].unique())

# Check if first column (index 0) contains only text with commas
print("\nFirst few values from column 0:")
print(df.iloc[1:6, 0].tolist())

# Check if column 1 has the actual labels
print("\nFirst few values from column 1 (potential labels):")
print(df.iloc[1:6, 1].tolist())