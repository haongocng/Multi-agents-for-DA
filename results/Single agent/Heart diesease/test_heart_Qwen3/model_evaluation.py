import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the trained model
model = joblib.load('trained_model.pkl')

# Load transformed test data (without target)
test_data = pd.read_csv('heart_test.csv')

# Preprocess test data the same way as training data
categorical_features = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak', 'FastingBS']

# Replace 0s in Cholesterol with NaN and convert to np.nan
test_data['Cholesterol'] = test_data['Cholesterol'].replace(0, np.nan)

# Load label encoders and scaler from training (recreate for consistency)
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Recreate label encoders
label_encoders = {}
for col in categorical_features:
    le = LabelEncoder()
    # Use known categories from training data
    known_categories = {
        'Sex': ['M', 'F'],
        'ChestPainType': ['ATA', 'NAP', 'ASY', 'TA'],
        'RestingECG': ['Normal', 'ST', 'LVH'],
        'ExerciseAngina': ['N', 'Y'],
        'ST_Slope': ['Up', 'Flat', 'Down']
    }
    
    # Fit label encoder on known categories
    le.fit(known_categories[col])
    label_encoders[col] = le
    # Encode test data
    test_data[col] = le.transform(test_data[col].astype(str))

# Impute missing values using np.nan (now properly handled)
imputer = SimpleImputer(strategy='median')
imputer.fit(test_data[numerical_features])
test_data[numerical_features] = imputer.transform(test_data[numerical_features])

# Scale numerical features
scaler = StandardScaler()
scaler.fit(test_data[numerical_features])
test_data[numerical_features] = scaler.transform(test_data[numerical_features])

# Make predictions
y_test_pred = model.predict(test_data)

# Save predictions to file
pd.DataFrame(y_test_pred, columns=['Predicted_HeartDisease']).to_csv('predictions.csv', index=False)

print("Predictions saved to 'predictions.csv'")