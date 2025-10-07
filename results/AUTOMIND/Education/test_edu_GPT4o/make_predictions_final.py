# Import necessary libraries
import pandas as pd
import joblib

# Load the transformed data
data_path = 'transformed_data.csv'
data = pd.read_csv(data_path)

# Drop the target column if it exists
target_column = 'I am willing to share my digital skills with other students'
if target_column in data.columns:
    data = data.drop(columns=[target_column])

# Load the trained model
model_path = 'trained_classification_model.pkl'
model = joblib.load(model_path)

# Make predictions
predictions = model.predict(data)

# Save predictions to a CSV file
data['Predictions'] = predictions
data.to_csv('predictions.csv', index=False)