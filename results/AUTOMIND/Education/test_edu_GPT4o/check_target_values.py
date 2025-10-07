import pandas as pd

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Check unique values of the target variable
y_unique_values = transformed_data['I am willing to share my digital skills with other students'].unique()
print(y_unique_values)