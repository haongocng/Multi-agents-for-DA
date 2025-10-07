import pandas as pd

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Handle outliers in Cholesterol: Cap at 99th percentile
q99_cholesterol = df['Cholesterol'].quantile(0.99)
df['Cholesterol'] = df['Cholesterol'].clip(upper=q99_cholesterol)

# Handle Oldpeak: Ensure non-negative values (based on medical plausibility)
df['Oldpeak'] = df['Oldpeak'].clip(lower=0)

# One-hot encode categorical variables
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Scale numerical features using StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
df_encoded[numerical_cols] = scaler.fit_transform(df_encoded[numerical_cols])

# Save transformed data
df_encoded.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Print summary
print("Transformed data shape:", df_encoded.shape)
print("\nFirst few rows of transformed data:")
print(df_encoded.head())
print("\nInfo of transformed DataFrame:")
df_encoded.info()