import pandas as pd

# Load the transformed dataset
df = pd.read_csv('transformed_data.csv', encoding='utf-8')

# Check the unique values in the target column to understand its nature
target_unique_values = df['I am willing to share my digital skills with other students'].unique()
target_unique_values