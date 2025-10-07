import joblib
import pandas as pd

# Try loading the model with joblib (alternative to pickle)
try:
    model = joblib.load('trained_classification_model.pkl')
    print("Model loaded successfully with joblib.")
except Exception as e:
    print(f"Error loading model with joblib: {e}")

# Try loading vectorizer with joblib
try:
    vectorizer = joblib.load('vectorizer.pkl')
    print("Vectorizer loaded successfully with joblib.")
except Exception as e:
    print(f"Error loading vectorizer with joblib: {e}")

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