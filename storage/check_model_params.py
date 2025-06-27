import joblib

# Load the trained model
model_path = 'trained_classification_model.pkl'
model = joblib.load(model_path)

# Print the model parameters
print(model.get_params())