import pickle

# Try to load the model with different protocol or check if it's corrupted
try:
    with open('trained_classification_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
    print(f"Model type: {type(model)}")
except Exception as e:
    print(f"Error loading model: {e}")