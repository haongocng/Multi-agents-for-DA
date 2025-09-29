import pandas as pd

# Load the dataset
filepath = 'heart_train.csv'
df = pd.read_csv(filepath, encoding='utf-8')

# Handle zero values in Cholesterol - treat as missing and impute with median
(df['Cholesterol'] == 0).sum()  # Check how many zeros
df['Cholesterol'] = df['Cholesterol'].replace(0, pd.NA)
df['Cholesterol'].fillna(df['Cholesterol'].median(), inplace=True)

# Encode categorical variables using One-Hot Encoding
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Scale numerical features using StandardScaler
from sklearn.preprocessing import StandardScaler
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak', 'FastingBS']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Create new features
# Interaction: Age * MaxHR (potential indicator of cardiovascular strain)
df['Age_MaxHR'] = df['Age'] * df['MaxHR']
# Ratio: Oldpeak / MaxHR (indicator of exercise stress response)
df['Oldpeak_MaxHR_Ratio'] = df['Oldpeak'] / (df['MaxHR'] + 1e-6)  # Avoid division by zero

# Save transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Print summary
print("Transformed data saved to transformed_data.csv")
print("\nInfo of transformed DataFrame:")
df.info()
print("\nFirst few rows of transformed data:")
print(df.head())