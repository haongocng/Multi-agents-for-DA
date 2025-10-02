import pandas as pd
# Load dataset
print("Loading dataset...")
df = pd.read_csv('heart_train.csv', encoding='utf-8')
print("Dataset loaded.")
# Basic information about the dataset
print("Basic information about the dataset:")
print(df.info())
print(df.head())
# Handle missing values
print("Handling missing values...")
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
print("Missing values after imputation:", df.isnull().sum())
# One-hot encoding for categorical variables
print("One-hot encoding for categorical variables...")
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df[['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']))
df = pd.concat([df.drop(['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'], axis=1), encoded_df], axis=1)
print("DataFrame after one-hot encoding:", df.head())
# Scale numerical features
print("Scaling numerical features...")
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Age_scaled'] = scaler.fit_transform(df[['Age']])
df['RestingBP_scaled'] = scaler.fit_transform(df[['RestingBP']])
df['Cholesterol_scaled'] = scaler.fit_transform(df[['Cholesterol']])
df['MaxHR_scaled'] = scaler.fit_transform(df[['MaxHR']])
df['Oldpeak_scaled'] = scaler.fit_transform(df[['Oldpeak']])
print("Numerical features after scaling:", df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']].head())
# Create new features
print("Creating new features...")
df['Age_x_RestingBP'] = df['Age'] * df['RestingBP']
df['Cholesterol_x_MaxHR'] = df['Cholesterol'] * df['MaxHR']
print("New features created:", df[['Age_x_RestingBP', 'Cholesterol_x_MaxHR']].head())
# Save transformed data
print("Saving transformed data...")
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
print("Transformed data saved to transformed_data.csv")
print("Info of transformed DataFrame:")
df.info()
print(df.head())
# Write feature engineering report
print("Writing feature engineering report...")
with open('feature_engineering_report.md', 'w') as f:
    f.write("Feature Engineering Report\n==========================\n\n")
    f.write("Handling missing values:\n")
    f.write(str(df.isnull().sum()) + "\n\n")
    f.write("One-hot encoding for categorical variables:\n")
    f.write(str(encoded_df.head()) + "\n\n")
    f.write("Scaling numerical features:\n")
    f.write(str(df[['Age_scaled', 'RestingBP_scaled', 'Cholesterol_scaled', 'MaxHR_scaled', 'Oldpeak_scaled']].head()) + "\n\n")
    f.write("Creating new features:\n")
    f.write(str(df[['Age_x_RestingBP', 'Cholesterol_x_MaxHR']].head()) + "\n\n")
print("Feature engineering report saved to feature_engineering_report.md")