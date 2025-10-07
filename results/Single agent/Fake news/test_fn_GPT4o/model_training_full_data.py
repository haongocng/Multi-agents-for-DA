import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the full train data with specified encoding and separator
try:
    full_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t')
except pd.errors.ParserError:
    full_data = pd.read_csv('train.csv', encoding='utf-8', sep='\t', on_bad_lines='skip')

# Remove any non-numeric entries from the 'label' column
full_data = full_data[full_data['label'].apply(lambda x: x.isdigit())]

# Convert 'label' column to integers
full_data['label'] = full_data['label'].astype(int)

# Feature Engineering
vectorizer = TfidfVectorizer(max_features=5000)
X_full = vectorizer.fit_transform(full_data['text'])
y_full = full_data['label']

# Splitting the data into train and validation sets
X_train_full, X_val_full, y_train_full, y_val_full = train_test_split(X_full, y_full, test_size=0.2, random_state=42)

# Initialize the best model
best_model = GradientBoostingClassifier(n_estimators=100)

# Train the model on the full dataset
best_model.fit(X_train_full, y_train_full)

# Save the trained model
joblib.dump(best_model, 'trained_model.pkl')

# Evaluate the model
y_pred_full = best_model.predict(X_val_full)
accuracy = accuracy_score(y_val_full, y_pred_full)
precision = precision_score(y_val_full, y_pred_full)
recall = recall_score(y_val_full, y_pred_full)
f1 = f1_score(y_val_full, y_pred_full)

# Summary of model training
summary = (
    f"Model training complete on full data. Performance metrics: "
    f"Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}."
)

# Print the summary to capture the output
print(summary)