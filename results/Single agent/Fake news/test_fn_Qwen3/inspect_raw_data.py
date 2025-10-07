import pandas as pd

# Load the sampled dataset and inspect the raw content to understand the delimiter issue
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first few rows to see how data is structured
print("First few rows of raw data:")
print(df.head())

# Check the first row to see how many columns there are
print("\nFirst row as list:", df.iloc[0].tolist())