import joblib
import pandas as pd

# Try loading the model with joblib instead of pickle
try:
    model = joblib.load('trained_classification_model.pkl')
    print("Model loaded successfully with joblib.")
except Exception as e:
    print(f"Error loading model with joblib: {e}")

# Load scaler
scaler = joblib.load('scaler.pkl')

# Load transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Separate features and target
X = transformed_data.drop(columns=['I am willing to share my digital skills with other students'])
y_true = transformed_data['I am willing to share my digital skills with other students']

# Ensure target is in 0-4 range (as used during training)
y_true = y_true - 1

# Apply scaling
X_scaled = scaler.transform(X)

# Make predictions
y_pred = model.predict(X_scaled)

# Add predictions to dataframe (convert back to 1-5 scale)
transformed_data['predicted_label'] = y_pred + 1

# Save predictions
transformed_data.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')
print(f'Shape of predictions: {transformed_data.shape}')