import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('heart_train.csv', encoding='utf-8')

# Handling missing values
# There are no missing values as per EDA

# Encoding categorical variables
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
df = pd.concat([df.drop(categorical_cols, axis=1), encoded_df], axis=1)

# Scaling numerical features
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Creating new features
# Interaction between 'Age' and 'Cholesterol'
df['Age_x_Cholesterol'] = df['Age'] * df['Cholesterol']

# Saving transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Output summary of the transformed DataFrame
print("Transformed data saved to transformed_data.csv")
print("\nInfo of transformed DataFrame:\n")
df.info()
print("\nHead of transformed DataFrame:\n", df.head())