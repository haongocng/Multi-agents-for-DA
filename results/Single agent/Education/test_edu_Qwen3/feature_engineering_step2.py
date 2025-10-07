import pandas as pd

# Load the dataset
data = pd.read_csv('edudata_english.csv')

# Identify categorical columns
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
print('Categorical columns:', categorical_columns)

# Identify numerical columns (excluding target)
target_column = 'I am willing to share my digital skills with other students'
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
if target_column in numerical_columns:
    numerical_columns.remove(target_column)
print('Numerical columns:', numerical_columns)

# Check unique values in the target variable
target_unique = data[target_column].unique()
print('Unique values in target variable:', sorted(target_unique))