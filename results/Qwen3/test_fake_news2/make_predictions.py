import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Load the trained model
with open('trained_classification_model.pkl', 'rb') as f:
    model = pickle.load(f)

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

# Initialize TF-IDF vectorizer with same parameters as during training
# (We assume max_features=5000 and stop_words='english' based on model_selection_report)
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')

# Fit TF-IDF on the full training data (we need to load full transformed data to get the fitted vectorizer)
# But note: the model was trained with a fitted TF-IDF, so we need to load that too.
# Since we didn't save the vectorizer separately, we need to refit on full transformed train data

# Load full transformed training data
train_full_df = pd.read_csv('full_transformed_train.csv', encoding='utf-8')

# Fit the vectorizer on the full training text
tfidf.fit(train_full_df['text'])

# Transform test data
test_features = tfidf.transform(test_df['text'])

# Make predictions
predictions = model.predict(test_features)

# Add predictions to test dataframe
test_df['predicted_label'] = predictions

# Save predictions to CSV
test_df.to_csv('predictions.csv', index=False)

print(f"Predictions saved to 'predictions.csv'")
print(f"Sample predictions: {predictions[:5]}")