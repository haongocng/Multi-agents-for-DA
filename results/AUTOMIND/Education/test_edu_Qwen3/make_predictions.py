import pickle
import pandas as pd

# Load the trained SVM model and scaler
with open('trained_classification_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Load the transformed data
transformed_data = pd.read_csv('transformed_data.csv')

# Separate features and target
X = transformed_data.drop(columns=['I am willing to share my digital skills with other students'])
y_true = transformed_data['I am willing to share my digital skills with other students']

# Ensure the target is in 0-4 range (as used during training)
y_true = y_true - 1

# Apply scaling to features
X_scaled = scaler.transform(X)

# Make predictions
y_pred = model.predict(X_scaled)

# Add predictions to dataframe
transformed_data['predicted_label'] = y_pred + 1  # Convert back to 1-5 scale

# Save predictions to CSV
transformed_data.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')
print(f'Shape of predictions: {transformed_data.shape}')