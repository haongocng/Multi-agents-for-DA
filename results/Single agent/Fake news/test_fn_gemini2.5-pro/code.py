
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the full training data
df_full = pd.read_csv("train.csv", encoding="utf-8", sep='\t')

# Clean the data
df_full = df_full[df_full['label'] != 'label']
df_full = df_full.dropna(subset=['text', 'label'])
df_full['label'] = df_full['label'].astype(int)

# Separate features and target
X = df_full['text']
y = df_full['label']

# Split data into training and a final hold-out test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Apply TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Train the Gradient Boosting model
final_model = GradientBoostingClassifier(random_state=42)
final_model.fit(X_train_tfidf, y_train)

# Save the final model
joblib.dump(final_model, "trained_model.pkl")

# Make predictions on the hold-out test set
y_pred = final_model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Final Model Evaluation on the hold-out test set from full data:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")

evaluation_results = [f"Accuracy: {accuracy:.4f}", f"Precision: {precision:.4f}", f"Recall: {recall:.4f}", f"F1-score: {f1:.4f}"]
