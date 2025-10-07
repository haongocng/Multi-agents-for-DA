
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("heart_train.csv")

# Separate target variable
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Identify categorical and numerical features
categorical_features = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
numerical_features = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]

# Create preprocessing pipelines for numerical and categorical features
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

# Create a preprocessor object using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features),
    ])

# Fit and transform the data
X_processed = preprocessor.fit_transform(X)

# Get the feature names after one-hot encoding
categorical_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)

# Combine numerical and new categorical feature names
feature_names = numerical_features + list(categorical_feature_names)

# Create a new DataFrame with the processed data
X_processed_df = pd.DataFrame(X_processed, columns=feature_names)

# Concatenate the processed features with the target variable
transformed_df = pd.concat([X_processed_df, y], axis=1)

# Save the transformed data
transformed_df.to_csv("transformed_data.csv", index=False)

print("Feature engineering complete. Transformed data saved to transformed_data.csv")
