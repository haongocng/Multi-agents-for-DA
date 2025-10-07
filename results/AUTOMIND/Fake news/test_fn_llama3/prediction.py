import pickle
import pandas as pd
# Load the trained model
with open('trained_classification_model.pkl', 'rb') as f:
    trained_model = pickle.load(f, fix_imports=True)
# Now trained_model should be your previously saved model
# Load the test data
test_data = pd.read_csv('test.csv', encoding='utf-8', sep='\t')
# Make predictions on the test data
predictions = trained_model.predict(test_data)
# Save the predictions to a new CSV file
import numpy as np
np.savetxt('predictions.csv', predictions, delimiter=',')
print('Predictions saved to predictions.csv')