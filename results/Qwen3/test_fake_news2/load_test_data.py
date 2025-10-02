import pandas as pd

# Load test data
test_df = pd.read_csv('test.csv', encoding='utf-8', sep='\t')

# Display first few rows to inspect structure
print(test_df.head())