import pickle
import pandas as pd

# Load the trained model and vectorizer
try:
    with open('trained_classification_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

try:
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    print("Vectorizer loaded successfully.")
except Exception as e:
    print(f"Error loading vectorizer: {e}")

# Load test data
test_data = pd.read_csv('test.csv', encoding='utf-8', sep='\t')

# Ensure text column exists and is string type
test_data['text'] = test_data['text'].astype(str)

# Apply the same vectorization used in training
test_features = vectorizer.transform(test_data['text'])

# Make predictions
predictions = model.predict(test_features)

# Add predictions to test data
test_data['prediction'] = predictions

# Save predictions to CSV
test_data.to_csv('predictions.csv', index=False)

print('Predictions saved to predictions.csv')