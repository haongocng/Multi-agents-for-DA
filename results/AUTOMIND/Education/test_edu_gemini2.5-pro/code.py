
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("transformed_data.csv")

# Load the trained model
model = joblib.load("trained_classification_model.pkl")

# Separate features and target
X = df.drop("I am willing to share my digital skills with other students", axis=1)
y = df["I am willing to share my digital skills with other students"]

# Make predictions
predictions = model.predict(X)

# Add predictions to the dataframe
df["predictions"] = predictions

# Save the dataframe with predictions
df.to_csv("predictions.csv", index=False)

print("Predictions made and saved to predictions.csv")
