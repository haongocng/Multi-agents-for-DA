import pandas as pd

# Load the transformed training data to inspect exact column names
train_transformed = pd.read_csv('transformed_data.csv')

# Display column names to see the exact feature names used in training
print('Training data columns:')
print(list(train_transformed.columns))

# Check the target column
print('\nTarget column (HeartDisease) exists:', 'HeartDisease' in train_transformed.columns)