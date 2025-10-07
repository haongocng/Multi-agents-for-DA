import pandas as pd

# Load the dataset
data = pd.read_csv('edudata_english.csv')

# Display column names and data types
column_info = data.dtypes.reset_index()
column_info.columns = ['Column', 'DataType']

# Check for missing values in each column
missing_values = data.isnull().sum().reset_index()
missing_values.columns = ['Column', 'MissingCount']

# Combine info
combined_info = column_info.merge(missing_values, on='Column')

# Display the first few rows of the combined info
combined_info.head(10)