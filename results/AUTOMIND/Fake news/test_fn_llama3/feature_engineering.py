import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('sampled_data.csv', encoding='utf-8')

df.target = df['label'].astype('category').cat.codes

df.drop('label', axis=1, inplace=True)

categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    encoded_features = encoder.fit_transform(df[[col]])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out([col]))
    df = pd.concat([df.drop(col, axis=1), encoded_df], axis=1)

numerical_cols = df.select_dtypes(include=['number']).columns

scaler = StandardScaler()
for col in numerical_cols:
    df[col + '_scaled'] = scaler.fit_transform(df[[col]])

df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
print("Transformed data saved to transformed_data.csv")
print("Info of transformed DataFrame:\n")
df.info()