import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load the test data
heart_test_data = pd.read_csv('heart_test.csv')

# Load the trained model
with open('trained_xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Apply the same feature engineering transformations
# Assuming the same transformations as in feature_engineering_report.md
# Encoding categorical features
heart_test_data = pd.get_dummies(heart_test_data, columns=['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])

# Scaling numerical features
scaler = StandardScaler()
heart_test_data[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']] = scaler.fit_transform(heart_test_data[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']])

# Creating interaction feature
heart_test_data['Age_x_Cholesterol'] = heart_test_data['Age'] * heart_test_data['Cholesterol']

# Ensure all columns match the training data
# Fill missing columns with zeros (for one-hot encoded columns that might not appear in the test set)
for col in model.feature_names_in_:
    if col not in heart_test_data.columns:
        heart_test_data[col] = 0

# Reorder the columns to match the training data
heart_test_data = heart_test_data[model.feature_names_in_]

# Generate predictions
predictions = model.predict(heart_test_data)

# Save predictions
heart_test_data['Predicted_HeartDisease'] = predictions
heart_test_data.to_csv('predictions.csv', index=False)