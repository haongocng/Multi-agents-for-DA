import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the test data
try:
    test_data = pd.read_csv('test.csv', encoding='utf-8', sep='\t', on_bad_lines='skip')
    test_data_shape = test_data.shape
except Exception as e:
    test_data_shape = str(e)

# Load the trained model and vectorizer
try:
    with open('trained_classification_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    model_loaded = True
except Exception as e:
    model_loaded = str(e)

# Output the results
output = f"Test data shape: {test_data_shape}, Model loaded: {model_loaded}"
output