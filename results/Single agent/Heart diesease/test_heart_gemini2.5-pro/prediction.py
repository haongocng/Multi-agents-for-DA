
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load test data
test_df = pd.read_csv("heart_test.csv")
X_test = test_df

# Load training data for fitting the preprocessor
train_df = pd.read_csv("heart_train.csv")
X_train = train_df.drop("HeartDisease", axis=1)

# Re-create the preprocessor from feature engineering
categorical_features = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
numerical_features = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]

numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features),
    ])

# Fit the preprocessor on the training data and transform the test data
preprocessor.fit(X_train)
X_test_processed = preprocessor.transform(X_test)

# Load the trained model
model = joblib.load("trained_model.pkl")

# Make predictions on the processed test data
predictions = model.predict(X_test_processed)

# Create a DataFrame with the predictions
predictions_df = pd.DataFrame(predictions, columns=["HeartDisease_Prediction"])

# Save the predictions to a CSV file
predictions_df.to_csv("heart_disease_predictions.csv", index=False)

print("Predictions generated and saved to heart_disease_predictions.csv")
