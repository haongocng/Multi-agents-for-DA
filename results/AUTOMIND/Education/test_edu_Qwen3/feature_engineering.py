import pandas as pd

# Load the dataset
filepath = 'edudata_english.csv'
df = pd.read_csv(filepath, encoding='utf-8')

# Target variable: 'I am willing to share my digital skills with other students'
target_col = 'I am willing to share my digital skills with other students'

# Check data types and missing values
print("Original data info:")
df.info()
print("\nMissing values before imputation:")
print(df.isnull().sum())

# Impute missing values: mean for numerical, mode for categorical
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values after imputation:")
print(df.isnull().sum())

# Encode categorical variables using One-Hot Encoding
from sklearn.preprocessing import OneHotEncoder

categorical_cols = ['Gender', 'Current Academic Year', 'Experience Using Digital Tools in Learning', 'Region of Your School']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))

# Drop original categorical columns and concatenate encoded ones
df = df.drop(categorical_cols, axis=1)
df = pd.concat([df, encoded_df], axis=1)

print("\nDataFrame shape after encoding:", df.shape)
print("\nFirst few rows of transformed data:")
print(df.head())

# Save transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
print("\nTransformed data saved to 'transformed_data.csv'")