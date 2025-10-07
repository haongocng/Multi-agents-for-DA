
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the transformed data
transformed_df = pd.read_csv("transformed_data.csv")

# Separate features and target
X = transformed_df.drop("HeartDisease", axis=1)
y = transformed_df["HeartDisease"]

# Initialize and train the Random Forest model
rand_forest = RandomForestClassifier(random_state=42)
rand_forest.fit(X, y)

# Save the trained model
joblib.dump(rand_forest, "trained_model.pkl")

print("Model training complete. Trained model saved to trained_model.pkl")
