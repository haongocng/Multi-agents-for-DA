import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle

# Load the sampled dataset
df = pd.read_csv('sampled_dataset.csv', encoding='utf-8')

# Handling Missing Values
# For numerical columns
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)
# For categorical columns
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Encoding Categorical Variables
# Assuming 'text' needs to be transformed using a text vectorizer, but since it's a sample, we'll use a simple encoding
# In a real scenario, a TfidfVectorizer would be more appropriate, but this is a placeholder
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_features = encoder.fit_transform(df[['label']])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['label']))
df = pd.concat([df.drop('label', axis=1), encoded_df], axis=1)

# Save the encoder
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)

# Scaling Numerical Features
# Placeholder for numerical features scaling, assume no numerical features in this sample
# scaler = StandardScaler()
# df['numerical_feature_scaled'] = scaler.fit_transform(df[['numerical_feature']])
# Save the scaler
# with open('numerical_scaler.pkl', 'wb') as f:
#     pickle.dump(scaler, f)

# Save Transformed Data
df.to_csv('transformed_data.csv', index=False, encoding='utf-8')

# Summary of the transformed DataFrame
data_summary = f"Transformed data saved to transformed_data.csv with shape {df.shape} and columns: {list(df.columns)}"
print(data_summary)