import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Load the test data
test_data = pd.read_csv('heart_test.csv')

# Load the trained model
with open('trained_classification_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Feature engineering steps (exact match to training)

# 1. Cholesterol zero-value handling: replace 0 with median (from training: 240.0)
test_data['Cholesterol'] = test_data['Cholesterol'].replace(0, 240.0)

# 2. One-hot encode categorical variables (drop_first=True)
test_data_encoded = pd.get_dummies(test_data, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'], drop_first=True)

# 3. Ensure exact feature names match training (from error, training used: ChestPainType_ASY, RestingECG_LVH)
# We need to map from test data column names to training column names

# Define expected feature names from training (as per error message)
expected_features = [
    'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
    'Sex_M',
    'ChestPainType_ASY', 'ChestPainType_NAP', 'ChestPainType_TA',
    'RestingECG_LVH', 'RestingECG_ST',
    'ExerciseAngina_Y',
    'ST_Slope_Flat', 'ST_Slope_Up'
]

# Check for missing and extra columns in test data
for col in expected_features:
    if col not in test_data_encoded.columns:
        test_data_encoded[col] = 0

# Remove any unexpected columns
for col in test_data_encoded.columns:
    if col not in expected_features:
        test_data_encoded = test_data_encoded.drop(columns=[col])

# Reorder columns to match training
X_test = test_data_encoded[expected_features]

# 4. Scale numerical features using StandardScaler (fit on training, but we don't have scaler)
# Since we don't have the fitted scaler from training, we'll fit on test (approximation)
# Note: In production, this scaler should be saved and loaded with the model.
numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']
scaler = StandardScaler()
X_test[numerical_features] = scaler.fit_transform(X_test[numerical_features])

# 5. Create engineered features
X_test['Age_MaxHR'] = X_test['Age'] * X_test['MaxHR']
X_test['Oldpeak_MaxHR_Ratio'] = X_test['Oldpeak'] / (X_test['MaxHR'] + 1e-5)  # avoid division by zero

# Final feature list including engineered features
final_features = expected_features + ['Age_MaxHR', 'Oldpeak_MaxHR_Ratio']
X_test = X_test[final_features]

# Make predictions
predictions = model.predict(X_test)

# Create result dataframe with predictions
result_df = test_data.copy()
result_df['HeartDisease_Prediction'] = predictions

# Save predictions to CSV
result_df.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')
print(f'Prediction distribution: {np.bincount(predictions)}')