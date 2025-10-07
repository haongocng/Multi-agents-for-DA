import pandas as pd
import joblib

# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Remove 'Timestamp' column if it exists
if 'Timestamp' in transformed_data.columns:
    transformed_data = transformed_data.drop(columns=['Timestamp'])
    print("'Timestamp' column removed from the dataset.")

# Separate features and target
X = transformed_data.drop(columns=['I am willing to share my digital skills with other students'])
y_true = transformed_data['I am willing to share my digital skills with other students']

# Ensure target is in 0-4 range (as used during training)
y_true = y_true - 1

# Load the trained model and scaler
model = joblib.load('trained_classification_model.pkl')
scaler = joblib.load('scaler.pkl')

# Apply scaling to features
X_scaled = scaler.transform(X)

# Make predictions
y_pred = model.predict(X_scaled)

# Add predictions to dataframe (convert back to 1-5 scale)
transformed_data['predicted_label'] = y_pred + 1

# Save predictions to CSV
transformed_data.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')
print(f'Shape of predictions: {transformed_data.shape}')