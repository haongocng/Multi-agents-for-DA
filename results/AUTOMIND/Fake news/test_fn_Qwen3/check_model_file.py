import os

# Check the size and first few bytes of the trained model file
model_path = 'trained_classification_model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        header = f.read(20)
        print(f"File size: {os.path.getsize(model_path)} bytes")
        print(f"First 20 bytes: {header}")
else:
    print("Model file not found.")