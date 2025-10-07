import pickle

# Try to load the model to check its integrity
try:
    with open('trained_classification_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
    print(type(model))
except Exception as e:
    print(f"Error loading model: {e}")