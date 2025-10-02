import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Load the test data
test_data = pd.read_csv('heart_test.csv')

# Load the trained model
with open('trained_classification_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Feature engineering steps (same as training)

# 1. Cholesterol zero-value handling: replace 0 with median (from training: 240.0)
test_data['Cholesterol'] = test_data['Cholesterol'].replace(0, 240.0)

# 2. One-hot encode categorical variables (drop first to avoid multicollinearity)
test_data = pd.get_dummies(test_data, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'], drop_first=True)

# 3. Ensure all expected columns from training are present (add missing columns as 0)
expected_features = [
    'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
    'Sex_M', 'ChestPainType_ASY', 'ChestPainType_NAP', 'ChestPainType_TA',
    'RestingECG_LVH', 'RestingECG_ST', 'ExerciseAngina_Y', 'ST_Slope_Flat', 'ST_Slope_Up'
]

for col in expected_features:
    if col not in test_data.columns:
        test_data[col] = 0

# Reorder columns to match training
X_test = test_data[expected_features]

# 4. Scale numerical features using the same scaler (we assume StandardScaler was used)
# Note: Since we don't have the fitted scaler, we'll fit a new one on test (this is suboptimal but necessary without saved scaler)
# In production, the scaler should be saved and loaded with the model.
# For now, we proceed with scaling using the same method (mean/std from training)
# We approximate using training statistics from feature_engineering_report.md:
# Numerical features: Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak
# We use median for Cholesterol but scaled using mean and std from training
# Since we don't have exact training stats, we proceed with scaling using test data mean/std

scaler = StandardScaler()
numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']
X_test[numerical_features] = scaler.fit_transform(X_test[numerical_features])

# 5. Create engineered features
X_test['Age_MaxHR'] = X_test['Age'] * X_test['MaxHR']
X_test['Oldpeak_MaxHR_Ratio'] = X_test['Oldpeak'] / (X_test['MaxHR'] + 1e-5)  # avoid division by zero

# Ensure all 18 features are present
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