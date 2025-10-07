import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

# Load the dataset
file_path = 'edudata_english.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Display initial info
initial_info = df.info()

# Handling missing values
# For numerical columns, impute with mean
numerical_cols = df.select_dtypes(include=['number']).columns
imputer_num = SimpleImputer(strategy='mean')
df[numerical_cols] = imputer_num.fit_transform(df[numerical_cols])

# For categorical columns, impute with mode
categorical_cols = df.select_dtypes(include=['object']).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_cat.fit_transform(df[categorical_cols])

# Encoding categorical variables using One-Hot Encoding
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_df = pd.DataFrame(encoder.fit_transform(df[categorical_cols]), columns=encoder.get_feature_names_out(categorical_cols))

# Drop original categorical columns and concatenate encoded columns
df.drop(categorical_cols, axis=1, inplace=True)
df = pd.concat([df, encoded_df], axis=1)

# Scaling numerical features
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Save the transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Display transformed data info
transformed_info = df.info()

# Return initial and transformed data info
initial_info, transformed_info