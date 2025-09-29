import pandas as pd

# Load the test data
test_data = pd.read_csv('heart_test.csv')

# Display first few rows to understand structure
print(test_data.head())

# Save the shape and info for verification
test_data.info()