import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Load the dataset
data = pd.read_csv('edudata_english.csv')

# Define features and target
feature_columns = [col for col in data.columns if col != 'I am willing to share my digital skills with other students']
target_column = 'I am willing to share my digital skills with other students'

# Separate features and target
X = data[feature_columns]
y = data[target_column]

# Identify categorical and numerical columns
categorical_columns = X.select_dtypes(include=['object']).columns.tolist()
numerical_columns = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Create preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_columns),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_columns)
    ]
)

# Apply preprocessing
X_processed = preprocessor.fit_transform(X)

# Convert processed features back to DataFrame for clarity
feature_names = (numerical_columns + 
                 list(preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_columns)))
X_processed_df = pd.DataFrame(X_processed, columns=feature_names)

# Save the processed data
X_processed_df.to_csv('transformed_data.csv', index=False)

# Save target variable separately
y.to_csv('target_labels.csv', index=False)

# Confirm shapes
print(f"Processed features shape: {X_processed_df.shape}")
print(f"Target shape: {y.shape}")