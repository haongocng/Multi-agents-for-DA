import pandas as pd

# Load the dataset as single column and inspect the raw content to understand the structure
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8', header=None)

# Display first 15 rows to fully understand the structure
print("First 15 rows of raw data:")
print(df.head(15))

# Check the type and content of the first row
print("\nFirst row (header):", df.iloc[0, 0])

# Check the type and content of the second row (first data row)
print("\nSecond row (first data row):", df.iloc[1, 0])

# Check if the label column has leading/trailing spaces
print("\nSample of label values (from second row onwards):")
for i in range(1, 6):
    row = df.iloc[i, 0]
    if ',' in row:
        parts = row.split(',', 1)
        print(f"Row {i}: text='{parts[0].strip()}', label='{parts[1].strip()}'")