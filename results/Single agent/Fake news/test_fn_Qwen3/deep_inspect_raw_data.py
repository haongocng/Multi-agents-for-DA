import pandas as pd

# Load the sampled dataset with no header and inspect raw content
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first 10 rows to fully understand structure
print("First 10 rows of raw data:")
print(df.head(10))

# Check if any rows have more than one comma
print("\nNumber of commas in each row:")
print(df[0].str.count(',').head(10))