import joblib

# Try loading the model using joblib instead of pickle
try:
    model = joblib.load('trained_classification_model.pkl')
    print("Model loaded successfully with joblib!")
    print(f"Model type: {type(model)}")
except Exception as e:
    print(f"Error loading model with joblib: {e}")