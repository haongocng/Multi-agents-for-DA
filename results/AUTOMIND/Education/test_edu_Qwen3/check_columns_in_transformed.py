import pandas as pd

# Load the transformed data to inspect column names
transformed_data = pd.read_csv('transformed_data.csv')

# Print column names
print("Columns in transformed_data:", list(transformed_data.columns))

# Check if 'Timestamp' is still present
if 'Timestamp' in transformed_data.columns:
    print("Warning: 'Timestamp' column is still in the dataset! It should have been removed during feature engineering.")
else:
    print("'Timestamp' column is correctly removed.")