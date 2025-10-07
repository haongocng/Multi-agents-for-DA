import pandas as pd

# Attempt to load the first few rows of the test data to inspect its structure
test_data_sample = pd.read_csv('test.csv', delimiter=',', on_bad_lines='skip', engine='python', nrows=5)

# Output the columns to understand the structure
columns = test_data_sample.columns

# Prepare a summary of the columns
summary = f"Columns in test data: {list(columns)}"

# Print the summary to capture the output
print(summary)