
import pandas as pd
import pickle

# Load the transformed test data
test_data = pd.read_csv("test_transformed.csv")

# Load the trained model
with open("trained_classification_model.pkl", "rb") as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(test_data)

# Save the predictions to a new CSV file
_ = pd.DataFrame({'predictions': predictions})
original_test_data = pd.read_csv("heart_test.csv")

# Add the predictions to the original test data as a new column
original_test_data['predicted_heart_disease'] = predictions
original_test_data.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")
