import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load cleaned data
df = pd.read_csv('train.csv', encoding='utf-8', sep='\t')
df = df[df['label'] != 'label']
df['label'] = df['label'].map({'0': 0, '1': 1})

# Feature engineering: CountVectorizer with max_features=5000 (same as in model selection)
vectorizer = CountVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train Naive Bayes on full dataset (no validation split since model selection already done)
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'trained_classification_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Calculate training performance metrics
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred, target_names=['Real', 'Fake'])

print(f"\n=== TRAINING PERFORMANCE ===")
print(f"Accuracy: {accuracy:.4f}")
print(f"\nClassification Report:\n{report}")