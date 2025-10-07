import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('edudata_english.csv')

# Drop the 'Timestamp' column as it is not useful for prediction
data.drop(columns=['Timestamp'], inplace=True)

# Encode categorical variables
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    if column != 'I am willing to share my digital skills with other students':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

# Split the data into features and target
X = data.drop(columns=['I am willing to share my digital skills with other students'])
y = data['I am willing to share my digital skills with other students']

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Save the transformed data
transformed_data = pd.DataFrame(X_scaled, columns=X.columns)
transformed_data['I am willing to share my digital skills with other students'] = y
transformed_data.to_csv('transformed_data.csv', index=False)

# Save feature engineering details
feature_engineering_details = {
    'Label Encoders': {col: le.classes_.tolist() for col, le in label_encoders.items()},
    'Scaler': 'StandardScaler applied to all features',
    'Train Test Split': '80% train, 20% test'
}

feature_engineering_details