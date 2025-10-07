import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
import joblib

# Load the test data with the correct delimiter
test_data = pd.read_csv('test.csv', delimiter='\t', on_bad_lines='skip', engine='python')

# Redefine and fit the vectorizer with the same parameters used during training
vectorizer = TfidfVectorizer(max_features=5000)
# Assuming the full training data is available for fitting the vectorizer
full_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t', on_bad_lines='skip')
full_data = full_data[full_data['label'].apply(lambda x: x.isdigit())]
full_data['label'] = full_data['label'].astype(int)
vectorizer.fit(full_data['text'])

# Feature Engineering on test data
X_test = vectorizer.transform(test_data['text'])

# Load the trained model
best_model = joblib.load('trained_model.pkl')

# Predict on the test data
y_test_pred = best_model.predict(X_test)

# Since we don't have true labels for the test set, we will output the predictions
# Prepare a summary of the predictions
summary = f"Predictions on test data complete. Total predictions made: {len(y_test_pred)}."

# Print the summary to capture the output
print(summary)