import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

# Load data
df = pd.read_csv('Customers.csv')

# Drop CustomerID (not useful for clustering)
df = df.drop('CustomerID', axis=1)

# Handle missing Profession values by filling with mode
mode_profession = df['Profession'].mode()[0]
df['Profession'] = df['Profession'].fillna(mode_profession)

# Encode categorical variables
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])  # Male=1, Female=0
df['Profession'] = label_encoder.fit_transform(df['Profession'])

# Select features for clustering
feature_cols = ['Gender', 'Age', 'Annual Income ($)', 'Spending Score (1-100)', 'Profession', 'Work Experience', 'Family Size']
X = df[feature_cols]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaled data
df_scaled = pd.DataFrame(X_scaled, columns=feature_cols)
df_scaled.to_csv('transformed_data.csv', index=False)

# Save scaler for future use (optional)
import joblib
joblib.dump(scaler, 'scaler.pkl')

print("Feature engineering completed. Scaled data saved to 'transformed_data.csv'")
print("Feature names:", feature_cols)