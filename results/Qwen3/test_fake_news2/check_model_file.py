import os

# Check the size and content of the trained model file
model_path = 'trained_classification_model.pkl'
if os.path.exists(model_path):
    print(f"Model file size: {os.path.getsize(model_path)} bytes")
    # Try to read first few bytes to see if it's corrupted
    with open(model_path, 'rb') as f:
        print(f"First 20 bytes: {f.read(20)}")
else:
    print("Model file not found.")