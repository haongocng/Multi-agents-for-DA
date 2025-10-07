import pandas as pd
import joblib

# Load the test data
test_data = pd.read_csv('heart_test.csv')

# Load the trained model
model = joblib.load('trained_classification_model.pkl')

# Apply the same feature engineering steps as in training
# 1. Outlier handling
test_data['Cholesterol'] = test_data['Cholesterol'].clip(upper=test_data['Cholesterol'].quantile(0.99))
test_data['Oldpeak'] = test_data['Oldpeak'].clip(lower=0)

# 2. One-hot encoding for categorical variables
# We'll use the same columns as in training
categorical_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
test_data_encoded = pd.get_dummies(test_data, columns=categorical_features, drop_first=True)

# 3. Ensure all expected columns from training are present (align with training feature set)
# Load transformed training data to get feature names
transformed_train = pd.read_csv('transformed_data.csv')
training_features = transformed_train.drop(columns=['HeartDisease']).columns.tolist()

# Align test data with training feature set
test_data_aligned = test_data_encoded.reindex(columns=training_features, fill_value=0)

# 4. Standard scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(transformed_train.drop(columns=['HeartDisease']))  # Fit on training data
test_data_scaled = scaler.transform(test_data_aligned)

# Make predictions
predictions = model.predict(test_data_scaled)

# Save predictions to CSV
test_data['HeartDisease_Prediction'] = predictions
test_data.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')
print('Shape of test data after preprocessing:', test_data_scaled.shape)