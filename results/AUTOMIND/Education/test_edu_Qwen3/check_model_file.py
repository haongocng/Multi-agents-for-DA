import os

# Check the size and content of the model file
model_path = 'trained_classification_model.pkl'
if os.path.exists(model_path):
    print(f"Model file size: {os.path.getsize(model_path)} bytes")
    # Try reading first few bytes to check for corruption
    with open(model_path, 'rb') as f:
        print(f"First 20 bytes: {f.read(20)}")
else:
    print("Model file not found.")