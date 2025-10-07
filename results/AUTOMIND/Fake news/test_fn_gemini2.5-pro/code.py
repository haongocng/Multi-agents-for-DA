
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline

# Load the full training data
df = pd.read_csv('train.csv', encoding='utf-8', sep='\t')

# Preprocessing
df.drop_duplicates(subset=['text'], inplace=True)
df['label'] = pd.to_numeric(df['label'], errors='coerce')
df.dropna(subset=['label'], inplace=True)

X = df['text']
y = df['label']

# Create a pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(solver='liblinear')),
])

# Define parameters for GridSearchCV a
parameters = {
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'clf__C': (0.5, 1.0, 1.5),
}

# Perform Grid Search
grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X, y)

# Train final model with best parameters
best_pipeline = grid_search.best_estimator_
best_pipeline.fit(X, y)

# Save the model
joblib.dump(best_pipeline, './trained_classification_model.pkl')

# Calculate and print performance metrics on the training data
y_pred = best_pipeline.predict(X)

print(f"Training Accuracy: {accuracy_score(y, y_pred)}")
print(f"Training Precision: {precision_score(y, y_pred)}")
print(f"Training Recall: {recall_score(y, y_pred)}")
print(f"Training F1-score: {f1_score(y, y_pred)}")
