import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# Load data
sample_train_datapath = 'sampled_dataset.csv'
df = pd.read_csv(sample_train_datapath, encoding='utf-8', sep='\t')
# Perform feature engineering
# Handle missing values
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])
# Encode categorical variables
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df.select_dtypes(include=['object']).values)
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(df.select_dtypes(include=['object']).columns.values.tolist()))
df = pd.concat([df.select_dtypes(include=['number']), encoded_df], axis=1)
# Scale numerical features
scaler = StandardScaler()
df[df.select_dtypes(include=['number']).columns] = scaler.fit_transform(df.select_dtypes(include=['number']))
# Save transformed data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')
# Create feature engineering report
with open('feature_engineering_report.md', 'w') as f:
    f.write('# Feature Engineering Report\n')
    f.write('Feature engineering performed on sampled dataset.\n')
print("Feature engineering performed on sampled dataset.")