import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Load the trained model using joblib
model = joblib.load('trained_classification_model.pkl')

# Load test data
test_df = pd.read_csv('test.csv', encoding='utf-8', sep='\t')

# Apply the same text preprocessing as in training
def preprocess_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
    return ''

test_df['text'] = test_df['text'].apply(preprocess_text)

# Use the same TF-IDF parameters from training report: max_features=7000, ngram_range=(1,2), stop_words='english'
# Note: The pipeline already includes the fitted TF-IDF, so we can use it directly

# Make predictions directly using the pipeline
predictions = model.predict(test_df['text'])

# Add predictions to test dataframe
test_df['predicted_label'] = predictions

# Save predictions to CSV
test_df.to_csv('predictions.csv', index=False)

print(f"Predictions saved to 'predictions.csv'")
print(f"Sample predictions: {predictions[:5]}")