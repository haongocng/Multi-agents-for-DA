import pandas as pd
import joblib

# Load the transformed dataset
transformed_data = pd.read_csv('transformed_data.csv')

# Load the trained model
model = joblib.load('trained_classification_model.pkl')

# Separate features and target variable
# The target variable is the last column: 'I am willing to share my digital skills with other students'
feature_columns = [col for col in transformed_data.columns if col != 'Timestamp' and col != 'I am willing to share my digital skills with other students']
X = transformed_data[feature_columns]
y = transformed_data['I am willing to share my digital skills with other students']

# Print shapes for verification
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")

# Get unique values in the target variable
print(f"Unique values in target variable: {y.unique()}")